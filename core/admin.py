from django.contrib import admin
from django.contrib.auth.models import User
import reversion

from models import Patient, HealthFacility, CaseInvestigator


class PatientAdmin(reversion.VersionAdmin):
    list_display = ('info_code', 'first_name', 'last_name', 'health_facility')
    search_fields = ['info_code', 'first_name', 'last_name']
    raw_id_fields = ('health_facility',)

    def get_queryset(self, request):

        qs = super(PatientAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(health_facility__caseinvestigator__user=request.user).distinct()
        return qs


class HealthFacilityAdmin(reversion.VersionAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def get_queryset(self, request):

        qs = super(HealthFacilityAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(caseinvestigator__user=request.user).distinct()
        return qs


class CaseInvestigatorAdmin(reversion.VersionAdmin):
    list_display = ['user', 'health_facility', 'is_admin']
    raw_id_fields = ('user', 'health_facility')


admin.site.register(Patient, PatientAdmin)

#admin.site.unregister(Organization)
#admin.site.unregister(OrganizationUser)
#admin.site.unregister(OrganizationOwner)


admin.site.register(HealthFacility, HealthFacilityAdmin)
admin.site.register(CaseInvestigator, CaseInvestigatorAdmin)
