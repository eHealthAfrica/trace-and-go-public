from django.db import models

# This will be saved in this structure
#
# {
#   "last_name": "Secnid",
#   "_uuid": "e1dab9b8-5ed4-4a9c-a237-ccb6dfdbe410",
#   "_bamboo_dataset_id": "",
#   "enter_number": "123",
#   "_tags": [
#     
#   ],
#   "_xform_id_string": "tutorial_5",
#   "meta\/instanceID": "uuid:e1dab9b8-5ed4-4a9c-a237-ccb6dfdbe410",
#   "caregiver_number": "123",
#   "formhub\/uuid": "7c677ce882f3405db08f36691d9cc532",
#   "first_name": "Name",
#   "_submission_time": "2014-11-12T14:56:05",
#   "age": "12",
#   "_geolocation": [
#     null,
#     null
#   ],
#   "_attachments": [
#     
#   ],
#   "_userform_id": "test_tutorial_5",
#   "_status": "submitted_via_web",
#   "_id": 62040
# }


class Patient(models.Model):

    uid = models.CharField(max_length=20, db_index=True, unique = True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    enter_number = models.CharField(max_length=250)
    caregiver_number = models.CharField(max_length=250)
    age = models.CharField(max_length=250)
    geolocation = models.CharField(max_length=250)

    etu = models.CharField(max_length=250)
    
    alive = models.BooleanField()
    
    json = models.TextField(editable=False)
    
