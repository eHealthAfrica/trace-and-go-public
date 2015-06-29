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
