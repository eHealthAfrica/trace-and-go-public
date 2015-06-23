from django.contrib import admin
import reversion

from models import Patient, HealthFacility, CaseInvestigator
from django.db.models import Q


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
    list_display = ['user', 'health_facility', 'is_admin', 'created', 'modified']
    raw_id_fields = ('user', 'health_facility')

    def get_readonly_fields(self, request, obj=None):
        if (obj
                and not request.user.is_superuser
                and not obj.health_facility.caseinvestigator_set.filter(user=request.user, is_admin=True).count()):
            return self.fields or [f.name for f in self.model._meta.fields]

        return super(CaseInvestigatorAdmin, self).get_readonly_fields(request, obj)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return CaseInvestigator.objects.filter(is_admin=True, user=request.user).count()

    def get_queryset(self, request):

        qs = super(CaseInvestigatorAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(Q(health_facility__caseinvestigator__user=request.user)).distinct()
        return qs


admin.site.register(Patient, PatientAdmin)
admin.site.register(HealthFacility, HealthFacilityAdmin)
admin.site.register(CaseInvestigator, CaseInvestigatorAdmin)
