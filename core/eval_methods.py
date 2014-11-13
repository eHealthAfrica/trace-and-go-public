########################
# THIS IS AN EXAMPLE !!!
########################
#
# This is the eval method to check what to do. Please overwrite for your needs
# or set a method in settins.py with the same parameters
# 
#from core.models import Messages
#from django.utils import timezone
from django.core.mail import send_mail
from etu.models import Patient

import string
import random
from core.backends import sms_send_telerivet, sms_send_twilio


def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



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




def eval_json(json, request):
    
    pat = Patient()

    uid = id_generator()

    #Check if the uid exists
    while Patient.objects.filter(uid = uid ).count() == 1:
        uid = id_generator()

    pat.uid = uid
    pat.first_name = json["first_name"]
    pat.last_name = json["last_name"]
    pat.enter_number = json["enter_number"]
    pat.caregiver_number = json["caregiver_number"]
    pat.age = json["age"]
    pat.geolocation = unicode(json["_geolocation"])
    pat.alive = True
    pat.etu = ""
    
    pat.json = unicode(json)

    pat.save()

    #Send the text messages
    text = "%s %s has the code %s" % (pat.first_name, pat.last_name, uid )
    sms_send_twilio(pat.enter_number, text)
    sms_send_twilio(pat.caregiver_number, text)

    return uid
    
    #If the age is 21 send a message
#     if "age" in json.keys() and json["age"] == "21":
#         
#         message = Messages()
#         
#         message.number = "+234 818 629 5584"
#         message.message = "Someone with the age 21 was submitted"
#         message.when_to_send = timezone.now()
#         message.hook_ip = request.META.get('REMOTE_ADDR')
#         message.hook_json_message = json
#         message.save()
#         
#         return message
#     
#     return