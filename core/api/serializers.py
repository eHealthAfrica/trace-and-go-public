from rest_framework import serializers

from etu.models import Patient


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('uid', 'first_name', 'last_name', 'enter_number', 
                  'caregiver_number', 'age', 'geolocation', 'etu', 'alive',
                  'json')
