from rest_framework import serializers

from core.models import (
    Patient,
    HealthFacility,
    CaseInvestigator,
)


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class HealthFacilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HealthFacility


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    health_facility_id = serializers.PrimaryKeyRelatedField(read_only=False, source='health_facility', queryset=HealthFacility.objects.all())
    health_facility_url = serializers.HyperlinkedRelatedField(view_name='healthfacility-detail', read_only=True, source='health_facility')
    health_facility = HealthFacilitySerializer(read_only=True)
    class Meta:
        model = Patient


class CaseInvestigatorSerializer(DynamicFieldsModelSerializer, serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = CaseInvestigator
        #fields = ['user']
        read_only_fields = ['is_admin', 'health_facility']
