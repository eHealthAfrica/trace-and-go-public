from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from core.models import (
    HealthFacility,
    CaseInvestigator,
    Patient,
)


class TestHealthFacilityModel(APITestCase):

    fixtures = ['initial_data.json']

    def create_health_facility(self):
        return HealthFacility.objects.create(name='Lund University Hospital')

    def create_user(self):
        return User.objects.create_user('test-user', 'hello@example.com', 'password')

    def test_add_case_investigator_explicit(self):
        self.assertEqual(HealthFacility.objects.count(), 0)
        self.assertEqual(CaseInvestigator.objects.count(), 0)
        health_facility, user = (
            self.create_health_facility(),
            self.create_user(),
        )
        case_investigator = CaseInvestigator.objects.create(
            user=user,
            health_facility=health_facility,
            is_admin=False
        )
        self.assertEqual(
            health_facility.caseinvestigator_set.first(), case_investigator)
        self.assertEqual(
            health_facility.caseinvestigator_set.first().user, user)

    def test_health_facility_add_case_investigator_implicit(self):
        health_facility, user = (
            self.create_health_facility(),
            self.create_user(),
        )
        self.assertEqual(health_facility.caseinvestigator_set.count(), 0)

        health_facility.add_user(user)
        self.assertEqual(health_facility.caseinvestigator_set.count(), 1)
        self.assertEqual(health_facility.caseinvestigator_set.first().user, user)
        self.assertIsInstance(health_facility.caseinvestigator_set.first(), CaseInvestigator)

    def test_permissions(self):
        """
        Assert that Patients in one HealthFacility are not visible to
        CaseInvestigators belong to other HealthFacilities.
        """
        user_1 = User.objects.create_user(
            'test-user-1', 'hello@example.com', 'password')
        health_facility_1 = HealthFacility.objects.create(name='Hospital 1')
        CaseInvestigator.objects.create(
            user=user_1,
            health_facility=health_facility_1,
            is_admin=False,
        )

        user_2 = User.objects.create_user(
            'test-user-2', 'hello@example.com', 'password')
        health_facility_2 = HealthFacility.objects.create(name='Hospital 2')
        CaseInvestigator.objects.create(
            user=user_2,
            health_facility=health_facility_2,
            is_admin=False,
        )

        patient = Patient(health_facility=health_facility_1)
        patient.save()

        self.client.login(username='test-user-1', password='password')
        # TODO: Since not all HTML templates are in place yet,
        # the standard way of specifying or URL:
        #
        #     client.get(reverse('patient-list'))
        #
        # throws a TemplateDoesNotExist error.
        response = self.client.get('/patients/.json')
        # Our first user belongs to health_facility_1, as does the patient.
        # Hence they should be able to retrieve a list of patients which includes
        # the patient just created.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['info_code'], patient.info_code)
        response = self.client.get('/health-facilities/.json')
        self.assertEqual(len(response.data), 1)

        self.client.login(username='test-user-2', password='password')
        response = self.client.get('/patients/.json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        response = self.client.get('/health-facilities/.json')
        self.assertEqual(len(response.data), 1)

        # Finally, assert that a superuser can view all HealthFacilities.
        User.objects.create_superuser(
            'test-user-3', 'hello@example.com', 'password')
        self.client.login(username='test-user-3', password='password')
        response = self.client.get('/health-facilities/.json')
        self.assertEqual(len(response.data), 2)
