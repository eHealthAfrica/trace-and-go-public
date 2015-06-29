from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from core.models import (
    HealthFacility,
    CaseInvestigator,
    Patient,
)


class TestPatientPermissions(APITestCase):

    fixtures = ['initial_data.json']
    allowed_user_username = 'test-user-1'
    allowed_user_password = 'password'

    def setUp(self):
        self.user = User.objects.create_user(
            self.allowed_user_username,
            'hello@example.com',
            self.allowed_user_password,
        )
        self.health_facility = HealthFacility.objects.create(name='Hospital X')
        CaseInvestigator.objects.create(
            user=self.user,
            health_facility=self.health_facility,
            is_admin=False,
        )
        self.patient = Patient(health_facility=self.health_facility)
        self.patient.save()

    def test_permissions_user_in_same_HF_can_view(self):
        """
        Assert that Patients in one HealthFacility are visible to
        CaseInvestigators belonging to that HealthFacility.
        """
        self.client.login(username=self.allowed_user_username,
                          password=self.allowed_user_password)

        # TODO: Since not all HTML templates are in place yet,
        # the standard way of specifying or URL:
        #
        #     client.get(reverse('patient-list'))
        #
        # throws a TemplateDoesNotExist error.
        response = self.client.get('/patients/.json')
        # Our first user belongs to the same HealthFacility as the Patient does.
        # Hence, the retrieved list should include the the patient just created.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['info_code'], self.patient.info_code)

        response = self.client.get('/health-facilities/.json')
        self.assertEqual(len(response.data), 1)

    def test_permissions_user_in_other_HF_can_not_view(self):
        """
        Assert that Patients in one HealthFacility are not visible to
        CaseInvestigators not belonging to that HealthFacility.
        """
        user = User.objects.create_user(
            'test-user-2', 'hello@example.com', 'password')
        health_facility = HealthFacility.objects.create(name='Hospital Y')
        CaseInvestigator.objects.create(
            user=user,
            health_facility=health_facility,
            is_admin=False,
        )
        self.client.login(username='test-user-2', password='password')

        response = self.client.get('/patients/.json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        response = self.client.get('/health-facilities/.json')
        self.assertEqual(len(response.data), 1)

    def test_permissions_superuser(self):
        """
        Finally, assert that a superuser can view all HealthFacilities.
        """
        User.objects.create_superuser(
            'superuser', 'hello@example.com', 'password')
        self.client.login(username='superuser', password='password')
        response = self.client.get('/health-facilities/.json')
        self.assertEqual(len(response.data), 1)
