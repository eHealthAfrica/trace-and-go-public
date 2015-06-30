from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from rest_framework import pagination
from rest_framework.response import Response

from django.db.models import Q

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
    serializer_class = PatientSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

    def get_queryset(self):
        request = self.request
        qs = Patient.objects.filter(health_facility__caseinvestigator__user=request.user).distinct()
        if request.user.is_superuser:
            qs = Patient.objects.all()
        return qs

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if request.accepted_renderer.format == 'html':
            return Response({'data': instance})
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request)
        if request.accepted_renderer.format == 'html':
            return Response({
                'data': page,
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link(),
                'page_number': paginator.page.number,
            })
        serializer = PatientSerializer(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


class IsHFAmdminOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, health_facility):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return health_facility.is_admin(request.user)


class HealthFacilityViewSet(TemplateNameMixin, viewsets.ModelViewSet):
    serializer_class = HealthFacilitySerializer
    permission_classes = (IsHFAmdminOrReadOnly,)

    def get_queryset(self):
        request = self.request
        qs = HealthFacility.objects.filter(caseinvestigator__user=request.user).distinct()
        if request.user.is_superuser:
            qs = HealthFacility.objects.all()
        return qs


class CaseInvestigatorViewSet(TemplateNameMixin, viewsets.ModelViewSet):
    serializer_class = CaseInvestigatorSerializer

    def get_queryset(self):
        request = self.request
        qs = CaseInvestigator.objects.filter(Q(health_facility__caseinvestigator__user=request.user)).distinct()
        if request.user.is_superuser:
            qs = CaseInvestigator.objects.all()
        return qs
