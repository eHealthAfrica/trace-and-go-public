from django.conf import settings
from django.db import models

class Patient(models.Model):

    uid = models.CharField(max_length=20, db_index=True, unique = True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    moh_id = models.CharField(max_length=250)
    enter_number = models.CharField(max_length=250)
    caregiver_number = models.CharField(max_length=250)

    etu = models.CharField(max_length=250, blank=True, null=True)

    json = models.TextField(editable=False)

    line_listing = models.TextField(editable=False, blank=True, null=True)


    def save(self, *args, **kwargs):
        #Check if the etu field has changed.

        if self.pk is not  None:
            oldItem = Patient.objects.get(pk=self.pk)

            if oldItem.etu != self.etu:
                #If the etu has changed send out a message to the caregiver
                text = "The patient %s %s has been assigned to %s" % (self.first_name, self.last_name, self.etu)
                settings.SMS_BACKEND(self.caregiver_number, text)

        super(Patient, self).save(*args, **kwargs) # Call the "real" save() method.
