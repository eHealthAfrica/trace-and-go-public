from rest_framework import serializers

from core.models import (
    Patient,
    HealthFacility,
    CaseInvestigator,
)


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class PatientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Patient


class HealthFacilitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = HealthFacility


class CaseInvestigatorSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = CaseInvestigator
