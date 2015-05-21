import random
import string
from amsel import wordings
from django.conf import settings
from django.db import models
from organizations.base import (OrganizationBase, OrganizationUserBase,
                                OrganizationOwnerBase)


def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class HealthFacility(OrganizationBase):
    pass


class CaseInvestigator(OrganizationUserBase):
    pass


class HealthFacilityAdministrator(OrganizationOwnerBase):
    pass


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
