from rest_framework import viewsets

from etu.models import Patient
from core.api.serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
