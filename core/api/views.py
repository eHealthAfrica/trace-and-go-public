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


class TemplateNameMixin:
    '''
    For the given ViewClass return [viewclass_list.html, viewclass.html]
    as the list of templates to try.
    '''
    def get_template_names(self):
        return ['%s_%s.html' % (self.__class__.__name__.lower(), self.action),
                '%s.html' % self.__class__.__name__.lower()]


class PatientViewSet(TemplateNameMixin, viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class HealthFacilityViewSet(TemplateNameMixin, viewsets.ModelViewSet):
    queryset = HealthFacility.objects.all()
    serializer_class = HealthFacilitySerializer


class CaseInvestigatorViewSet(TemplateNameMixin, viewsets.ModelViewSet):
    queryset = CaseInvestigator.objects.all()
    serializer_class = CaseInvestigatorSerializer
