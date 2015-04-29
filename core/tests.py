from core.views import PATIENT_REGEX
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
import re

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from models import Patient


class TestHTTPServer(TestCase):

    def _delete_post_key(self):
        # Make sure we have security disabled
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
        self.assertEqual(response.status_code, 400)  # 400 Bad Request

        # Bad post key
        response = self.client.post("%s?key=something" % reverse('submit'))
        self.assertEqual(response.status_code, 403)  # 403 Forbidden

    def test_bad_post_keys(self):
        """
        We should only submit one JSON
        """
        self._delete_post_key()

        response = self.client.post(reverse('submit'), {"A": "A", "B": "B"})
        self.assertEqual(response.status_code, 400)  # 400 Bad Request

    def test_bad_json(self):
        """
        Json has to be valid
        """

        self._delete_post_key()

        response = self.client.post(reverse('submit'), {"Something that is not JSON": ""})
        self.assertEqual(response.status_code, 400)  # 400 Bad Request


class SMSInterfaceTests(TestCase):

    def test_number_formatter(self):
        """
        Checks that the number is formatted nicely
        """

        mes = sms_send_test("+1 800-642-7676", "testing")

        # Check that the return is correct
        self.assertEqual(mes, json.dumps({'phone': "+18006427676", 'text': "testing"}))

    def test_bad_number(self):
        '''
        Checks that a bad number just returns the number
        In the future this will create some sort of error
        '''

        mes = sms_send_test("+1123", "testing")

        # Check that the return is correct
        self.assertEqual(mes, json.dumps({'phone': "+1123", 'text': "testing"}))


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

    def test_new_formhub_submit(self):
        """
        Try to submit a new patient as formhub would
        """
        test_data = '{\
            "last_name": "Bob",\
            "_uuid": "934dd0ed-a956-4224-a36f-f9c71da5b229",\
            "_bamboo_dataset_id": "",\
            "enter_number": "12345678",\
            "moh_id": "Tbhi",\
            "_tags": [],\
            "_xform_id_string": "amsel",\
            "meta/instanceID": "uuid:934dd0ed-a956-4224-a36f-f9c71da5b229",\
            "caregiver_number": "123456799",\
            "formhub/uuid": "e35066ee71c44067872f048deacc1b89",\
            "first_name": "Monty",\
            "_submission_time": "2014-12-11T17:09:15",\
            "_geolocation": [\
                "",\
                ""\
            ],\
            "_attachments": [],\
            "_userform_id": "ebolalr_amsel",\
            "_status": "submitted_via_web",\
            "_id": "85971"\
        }'

        settings.SMS_BACKEND = sms_send_test

        length_before = len(Patient.objects.all())

        response = self.client.post('/submit', test_data, content_type="application/json")

        patient_code_regex = re.compile(PATIENT_REGEX)
        self.assertTrue(patient_code_regex.match(response.content))

        length_after = len(Patient.objects.all())

        self.assertEqual(length_before + 1, length_after)
        self.assertEqual(response.status_code, 200)

    def test_get_patients_not_authenticated(self):
        """
        See that /api/*/ returns a 403 if not authenticated
        """
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 403)

        response = self.client.get('/api/patients/')
        self.assertEqual(response.status_code, 403)

    def test_search_patients_authenticated(self):
        """
        See that /api/patients/?search=q returns patients that fullfil those
        search requirements.
        """

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        search_term = 'Jane'
        response = self.client.get('/api/patients/?search=%s' % (search_term))

        for obj in response.data:
            self.assertTrue(obj['first_name'] == search_term or
                            obj['last_name'] == search_term)
        self.assertEqual(response.status_code, 200)

    def test_filter_patients_authenticated(self):
        """
        See that /api/patients/?search=q returns patients that fullfil those
        search requirements.
        """

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        filter_value = u"Doe"
        response = self.client.get('/api/patients/?last_name=%s' % (filter_value))

        for obj in response.data:
            self.assertEqual(obj['last_name'], filter_value)
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

    def test_post_new_patient_authenticated(self):
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
            "moh_id": "123",
            "enter_number": "+182311121",
            "caregiver_number": "+123111811"
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.post('/api/patients/', data)

        length_after = len(Patient.objects.all())

        self.assertEqual(response.data['uid'], '1234')
        self.assertEqual(length_before + 1, length_after)
        self.assertEqual(response.status_code, 201)

    def test_patch_patient_authenticated(self):
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
