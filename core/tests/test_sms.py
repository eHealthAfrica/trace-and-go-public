from mock import MagicMock, call
from rest_framework.test import APITestCase
from django.test.utils import override_settings
from core.models import (
    Patient, HealthFacility
)

from core import tasks

from amsel import wordings

class TestSMSSending(APITestCase):

    contact_phone_number = '123'
    first_name = 'Bob'
    last_name = 'Bill'

    def create_patient(self, status):
        hf = HealthFacility()
        hf.name = 'HF'
        hf.save()
        self.health_facility = hf
        patient = Patient()
        patient.health_facility = hf
        if status:
            patient.status = status
        patient.contact_phone_number = self.contact_phone_number
        patient.first_name = self.first_name
        patient.last_name = self.last_name
        self.info_code = patient.info_code
        self.patient = patient
        return patient

    def assert_calls(self, mock, call_keys):
        calls = {
            'location': call(
                '123', wordings.patient_location % {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'health_facility': self.health_facility,
                    }),
            'changes': call(
                '123', wordings.initial_message),
            'status': call(
                '123', wordings.patient_status % {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'status': self.patient.get_status_display(),
                }),
            'patient_info': call(
                '123', wordings.patient_info % {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'info_code': self.info_code})}
        for ck in call_keys:
            mock.assert_has_call(calls.get(ck))

    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
    def test_send_sms(self):
        tasks.sms_func = MagicMock()
        p = self.create_patient(status='S')
        p.save()
        self.assertEqual(tasks.sms_func.call_count, 4)
        self.assert_calls(
            tasks.sms_func, [
                'location',
                'status',
                'changes',
                'patient_info',
                ])

