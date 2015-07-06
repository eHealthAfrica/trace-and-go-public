from django.contrib import admin
from django.db.models import Q
from django.core.exceptions import PermissionDenied

import reversion

from models import Patient, HealthFacility, CaseInvestigator


def has_admin_edit_permissions(user):
    """
    Returns True if 'user' is a superuser *or* a registered
    CaseInvestigator with admin permissions.
    """
    if user.is_superuser:
        return True
    try:
        case_investigator = CaseInvestigator.objects.get(user=user)
        return case_investigator.is_admin
    except CaseInvestigator.DoesNotExist:
        return False


class AdminEditOnlyMixIn(reversion.VersionAdmin):
    """
    Mixin which can be used to limit the actions of non-admin
    CaseInvestigators.
    """

    def has_add_permission(self, request, obj=None):
        return has_admin_edit_permissions(request.user)

    def has_delete_permission(self, request, obj=None):
        return has_admin_edit_permissions(request.user)

    def save_model(self, request, obj, form, change):
        """
        If user is not allowed to edit form, raise PermissionDenied (403).
        """
        if has_admin_edit_permissions(request.user):
            return super(reversion.VersionAdmin, self).save_model(
                request, obj, form, change)
        else:
            raise PermissionDenied


class PatientAdmin(reversion.VersionAdmin):
    list_display = ('info_code', 'first_name', 'last_name', 'health_facility')
    search_fields = ('info_code', 'first_name', 'last_name')
    raw_id_fields = ('health_facility',)
    readonly_fields = ('info_code',)

    def get_queryset(self, request):
        qs = super(PatientAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(health_facility__caseinvestigator__user=request.user).distinct()
        return qs


class HealthFacilityAdmin(AdminEditOnlyMixIn, reversion.VersionAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def get_queryset(self, request):
        qs = super(HealthFacilityAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(caseinvestigator__user=request.user).distinct()
        return qs


class CaseInvestigatorAdmin(AdminEditOnlyMixIn, reversion.VersionAdmin):
    list_display = ['user', 'health_facility', 'is_admin', 'created', 'modified']
    raw_id_fields = ('user', 'health_facility')

    def get_readonly_fields(self, request, obj=None):
        if (obj
                and not request.user.is_superuser
                and not obj.health_facility.caseinvestigator_set.filter(
                    user=request.user, is_admin=True).count()):
            return self.fields or [f.name for f in self.model._meta.fields]

        return super(CaseInvestigatorAdmin, self).get_readonly_fields(request, obj)

    def get_queryset(self, request):
        qs = super(CaseInvestigatorAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(Q(health_facility__caseinvestigator__user=request.user)).distinct()
        return qs


admin.site.site_header = 'Trace-And-Go'
admin.site.register(Patient, PatientAdmin)
admin.site.register(HealthFacility, HealthFacilityAdmin)
admin.site.register(CaseInvestigator, CaseInvestigatorAdmin)
