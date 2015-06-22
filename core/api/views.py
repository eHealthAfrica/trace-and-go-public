from rest_framework import viewsets
from rest_framework import filters

from core.models import (
    Patient,
    HealthFacility,
    CaseInvestigator,
    )
from core.api.serializers import (
    PatientSerializer,
    HealthFacilitySerializer,
    CaseInvestigatorSerializer,
    )


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class HealthFacilityViewSet(viewsets.ModelViewSet):
    queryset = HealthFacility.objects.all()
    serializer_class = HealthFacilitySerializer


class CaseInvestigatorViewSet(viewsets.ModelViewSet):
    queryset = CaseInvestigator.objects.all()
    serializer_class = CaseInvestigatorSerializer
