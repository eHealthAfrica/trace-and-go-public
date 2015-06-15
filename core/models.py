import random
import string
from amsel import wordings
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from organizations.models import (TimeStampedModel, SlugField)
from django.utils.translation import ugettext_lazy as _


def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class HealthFacility(TimeStampedModel):
    name = models.CharField(max_length=250, blank=False)
    slug = SlugField(max_length=250, blank=False, editable=True,
                     populate_from='name', unique=True,
                     help_text=_("The name in all lowercase, suitable for URL identification"))

    def __unicode__(self):
        return self.name

    def add_user(self, user, is_admin=False):
        """
        Adds a new user and if the first user makes the user an admin and
        the owner.
        """
        users_count = self.users.all().count()
        if users_count == 0:
            is_admin = True
        # TODO get specific org user?
        org_user = CaseInvestigator.objects.create(user=user,
                                                   health_facility=self, is_admin=is_admin)

        return org_user

    def remove_user(self, user):
        """
        Deletes a user from an health_facility.
        """
        org_user = CaseInvestigator.objects.get(user=user,
                                                health_facility=self)
        org_user.delete()

    def get_or_add_user(self, user, **kwargs):
        """
        Adds a new user to the health_facility, and if it's the first user makes
        the user an admin and the owner. Uses the `get_or_create` method to
        create or return the existing user.
        `user` should be a user instance, e.g. `auth.User`.
        Returns the same tuple as the `get_or_create` method, the
        `CaseInvestigator` and a boolean value indicating whether the
        CaseInvestigator was created or not.
        """
        is_admin = kwargs.pop('is_admin', False)
        users_count = self.users.all().count()
        if users_count == 0:
            is_admin = True

        org_user, created = CaseInvestigator.objects.get_or_create(
            health_facility=self, user=user, defaults={'is_admin': is_admin})

        return org_user, created

    def change_owner(self, new_owner):
        """
        Changes ownership of an health_facility.
        """
        self.owner.case_investigator = new_owner
        self.owner.save()

    def is_admin(self, user):
        """
        Returns True is user is an admin in the health_facility, otherwise false
        """
        return True if self.case_investigators.filter(user=user, is_admin=True) else False


class CaseInvestigator(TimeStampedModel):
    is_admin = models.BooleanField(default=False)
    health_facility = models.ForeignKey(HealthFacility)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u"{0} ({1})".format(self.user, self.health_facility.name)


class Patient(models.Model):
    info_code = models.CharField(max_length=20, db_index=True, unique=True, default=id_generator)
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    case_id = models.CharField(max_length=250, blank=True)
    contact_phone_number = models.CharField(max_length=250, blank=True)
    health_facility = models.ForeignKey(HealthFacility)

    PATIENT_STATUS = (
        ("A", "Just admitted"),
        ("S", "Stable"),
        ("C", "Condition not improving"),
        ("G", "Getting better"),
        ("D", 'You will receive a call from the doctor'),
        ("O", "Discharged"),
    )

    status = models.CharField(choices=PATIENT_STATUS, max_length=1, blank=True)

    line_listing = models.TextField(editable=False, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s %s' % (self.info_code, self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if self.contact_phone_number:

            if self.pk is not None:
                oldItem = Patient.objects.get(pk=self.pk)

                if oldItem.health_facility_id != self.health_facility_id:
                    # If the health facility has changed send out a message to the caregiver
                    mapping = {
                        'first_name': self.first_name,
                        'second_name': self.last_name,
                        'h_facility': self.health_facility
                    }

                    text = wordings.patient_location % mapping
                    settings.SMS_BACKEND(self.contact_phone_number, text)

                if oldItem.status != self.status:
                    # If the status has changed send out a message to the caregiver
                    mapping = {
                        'first_name': self.first_name,
                        'second_name': self.last_name,
                        'status': self.get_status_display()
                    }

                    text = wordings.patient_status % mapping
                    settings.SMS_BACKEND(self.contact_phone_number, text)

            else:
                # Send the text messages
                mapping = {
                    'first_name': self.first_name,
                    'second_name': self.last_name,
                    'info_code': self.info_code
                }

                text = wordings.patient_info % mapping

                if self.contact_phone_number:
                    settings.SMS_BACKEND(self.contact_phone_number, text)

                settings.SMS_BACKEND(self.contact_phone_number, wordings.initial_message)

                if self.health_facility:
                    mapping = {
                        'first_name': self.first_name,
                        'second_name': self.last_name,
                        'h_facility': self.health_facility
                    }

                    text = wordings.patient_location % mapping
                    settings.SMS_BACKEND(self.contact_phone_number, text)

                if self.status:
                    mapping = {
                        'first_name': self.first_name,
                        'second_name': self.last_name,
                        'status': self.get_status_display()
                    }

                    text = wordings.patient_status % mapping
                    settings.SMS_BACKEND(self.contact_phone_number, text)

        super(Patient, self).save(*args, **kwargs)  # Call the "real" save() method.


# Signals

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(pre_save, sender=CaseInvestigator)
def my_handler(sender, instance, **kwargs):
    group = Group.objects.get(name='Case Investigators')
    instance.user.groups.add(group)
    instance.user.is_staff = True
    instance.user.save()
