from rest_framework import serializers

from core.models import (
    Patient,
    HealthFacility,
    CaseInvestigator,
    )


class PatientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Patient


class HealthFacilitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = HealthFacility


class CaseInvestigatorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CaseInvestigator
