from rest_framework import serializers

from core.models import Patient


class PatientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Patient
