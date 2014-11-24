from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone
from core.backends import sms_send_test
import time
from django.core.management import call_command
import json
import datetime
# Create your tests here.


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

        
