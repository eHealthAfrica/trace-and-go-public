from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import list_route

import rest_framework_filters as filters

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


class PatientFilter(filters.FilterSet):
    first_name = filters.AllLookupsFilter(name='first_name')
    last_name = filters.AllLookupsFilter(name='last_name')
    info_code = filters.AllLookupsFilter(name='info_code')
    status = filters.AllLookupsFilter(name='status')

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'info_code', 'status']


class PatientViewSet(TemplateNameMixin, viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    filter_class = PatientFilter

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PatientViewSet, self).dispatch(request, *args, **kwargs)

    @list_route(url_path='add')
    def add(self, request, *args, **kwargs):
        return Response()

    def get_queryset(self):
        request = self.request
        qs = Patient.objects.filter(health_facility__caseinvestigator__user=request.user).distinct()
        if request.user.is_superuser:
            qs = Patient.objects.all()
        contains = self.request.query_params.get('contains', None)
        if contains:
            qs = qs.filter(
                Q(first_name__icontains=contains) | Q(last_name__icontains=contains) | Q(info_code__icontains=contains)
            )
        return qs.order_by('-pk')


class IsHFAmdminOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_superuser
        return request.user.is_authenticated()

    def has_object_permission(self, request, view, health_facility):
        if request.method == 'POST':
            return request.user.is_superuser
        return health_facility.id in HealthFacility.objects.filter(caseinvestigator__user=request.user).distinct().values_list('id', flat=True)


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            return False
        return request.method in permissions.SAFE_METHODS


class HealthFacilityViewSet(TemplateNameMixin, viewsets.ModelViewSet):
    serializer_class = HealthFacilitySerializer
    permission_classes = (IsHFAmdminOrReadOnly,)
    paginate_by_param = 'limit'

    def get_queryset(self):
        request = self.request
        qs = HealthFacility.objects.filter(caseinvestigator__user=request.user).distinct()
        if request.user.is_superuser:
            qs = HealthFacility.objects.all()
        return qs


class CaseInvestigatorViewSet(TemplateNameMixin, viewsets.ModelViewSet):
    serializer_class = CaseInvestigatorSerializer
    permission_classes = (ReadOnly,)

    def get_queryset(self):
        request = self.request
        qs = CaseInvestigator.objects.filter(Q(health_facility__caseinvestigator__user=request.user)).distinct()
        if request.user.is_superuser:
            qs = CaseInvestigator.objects.all()
        return qs
