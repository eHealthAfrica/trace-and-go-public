from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone
from core.backends import sms_send_test
import time
from django.core.management import call_command
import json
import datetime
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from etu.models import Patient


test_post = '{"_id": 115628, "_attachments": [], "name": "testing", "_submission_time": "2014-08-05T17:14:25", "age": "21", "_uuid": "0efee5c4-6bcb-4f92-8abd-8f631eb0270a", "_bamboo_dataset_id": "", "_tags": [], "_geolocation": [null, null], "_xform_id_string": "tutorial_tutorial", "_userform_id": "a_tutorial_tutorial", "_status": "submitted_via_web", "meta/instanceID": "uuid:0efee5c4-6bcb-4f92-8abd-8f631eb0270a", "has_children": "0", "formhub/uuid": "17d3747ce512463988f596cd847d0fcf"}'



class TestHTTPServer(TestCase):
    
    def _delete_post_key(self):
        #Make sure we have security disabled
        if getattr(settings, "POST_KEY", False):
            del settings.POST_KEY

    
    def test_get_will_fail(self):
        """
        We should not be able to use get on the /submit url
        """
        response = self.client.get(reverse('submit'))
        self.assertEqual(response.status_code, 405)
        
    def test_post_without_api_key(self):
        """
        If we have a POST_KEY set it should require it
        """

        settings.POST_KEY = "abc"

        # No post key        
        response = self.client.post(reverse('submit'))
        self.assertEqual(response.status_code, 400) # 400 Bad Request
        
        # Bad post key
        response = self.client.post("%s?key=something" % reverse('submit'))
        self.assertEqual(response.status_code, 403) # 403 Forbidden

    def test_bad_post_keys(self):
        """
        We should only submit one JSON
        """
        self._delete_post_key()

        response = self.client.post(reverse('submit'), {"A":"A", "B":"B"})
        self.assertEqual(response.status_code, 400) # 400 Bad Request


    def test_bad_json(self):
        """
        Json has to be valid
        """
        
        self._delete_post_key()
            
        response = self.client.post(reverse('submit'), {"Something that is not JSON":""})
        self.assertEqual(response.status_code, 400) # 400 Bad Request

        
class PatientViewSetTests(TestCase):
    fixtures = ['patient.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email="admin@admin.com",
            password="admin123",
            username="admin",
            is_superuser=True)
        self.token = Token.objects.create(user=self.user)

    def test_get_patients_not_authenticated(self):
        """
        See that /api/patients/ returns a list of all patients.
        """
        length = len(Patient.objects.all())
        response = self.client.get('/api/patients/')
        self.assertEqual(len(response.data), length)
        self.assertEqual(response.status_code, 200)

    def test_search_patients_not_authenticated(self):
        """
        See that /api/patients/?search=q returns patients that fullfil those
        search requirements.
        """
        search_term = 'Jane'
        response = self.client.get('/api/patients/?search=%s' % (search_term))

        for obj in response.data:
            self.assertTrue(obj['first_name'] == search_term or 
                obj['last_name'] == search_term)
        self.assertEqual(response.status_code, 200)

    def test_filter_patients_not_authenticated(self):
        """
        See that /api/patients/?search=q returns patients that fullfil those
        search requirements.
        """
        filter_value = True
        response = self.client.get('/api/patients/?alive=%s' % (filter_value))

        for obj in response.data:
            self.assertEqual(obj['alive'], filter_value)
        self.assertEqual(response.status_code, 200)

    def test_post_new_patient_not_authenticated(self):
        """
        See that /api/patients/?search=q returns patients that fullfil those
        search requirements.
        """
        data = {
            "geolocation": "31.11",
            "first_name": "Mark",
            "last_name": "Doe",
            "uid": "1234",
            "etu": "Test.",
            "age": "27",
            "enter_number": "+182311121",
            "alive": "false",
            "caregiver_number": "+123111811"
            }
        response = self.client.post('/api/patients/', data)

        self.assertEqual(response.status_code, 403)

    def test_post_new_patient_not_authenticated(self):
        """
        See that /api/patients/?search=q returns patients that fullfil those
        search requirements.
        """

        length_before = len(Patient.objects.all())

        data = {
            "geolocation": "31.11",
            "first_name": "Mark",
            "last_name": "Doe",
            "uid": "1234",
            "etu": "Test.",
            "age": "27",
            "enter_number": "+182311121",
            "alive": "false",
            "caregiver_number": "+123111811"
            }
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        response = self.client.post('/api/patients/', data)

        length_after = len(Patient.objects.all())

        self.assertEqual(response.data['uid'], '1234')
        self.assertEqual(length_before + 1, length_after)
        self.assertEqual(response.status_code, 201)

    def test_patch_patient_not_authenticated(self):
        """
        See that /api/patients/?search=q returns patients that fullfil those
        search requirements.
        """

        patient = Patient.objects.all().first()
        data = {
            "first_name": "Janice"
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = '/api/patients/%s/' % (patient.pk)
        response = self.client.patch(url, data)
        updated_patient = Patient.objects.all().first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_patient.first_name, 'Janice')
        
        
