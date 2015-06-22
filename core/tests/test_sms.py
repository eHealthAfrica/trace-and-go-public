from mock import MagicMock
from rest_framework.test import APITestCase
from django.test.utils import override_settings
from core.models import (
    Patient, HealthFacility
)

from core import tasks


class TestSMSSending(APITestCase):

    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
    def test_send_sms(self):
        hf = HealthFacility()
        hf.name = 'HF'
        hf.save()
        tasks.sms_func = MagicMock()
        p = Patient()
        p.health_facility = hf
        p.contact_phone_number = '123'
        p.first_name = 'Bob'
        p.last_name = 'Bill'
        p.save()
        tasks.sms_func.assert_called_with('123', 'The patient Bob Bill is at HF')
