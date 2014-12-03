from rest_framework import viewsets
from rest_framework import filters

from etu.models import Patient
from core.api.serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    filter_fields = ('alive', 'age', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
