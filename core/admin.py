from django.contrib import admin
import reversion

from models import Patient, HealthFacility, HealthFacilityAdministrator, CaseInvestigator
from organizations.models import (Organization, OrganizationUser,
                                  OrganizationOwner)
from .forms import CaseInvestigatorForm


class PatientAdmin(reversion.VersionAdmin):
    list_display = ('info_code', 'first_name', 'last_name', 'health_facility')
    search_fields = ['info_code', 'first_name', 'last_name']


class CaseInvestigatorAdmin(admin.ModelAdmin):
    form = CaseInvestigatorForm

# Register your models here.
admin.site.register(Patient, PatientAdmin)

admin.site.unregister(Organization)
admin.site.unregister(OrganizationUser)
admin.site.unregister(OrganizationOwner)


admin.site.register(HealthFacility)
admin.site.register(HealthFacilityAdministrator)
admin.site.register(CaseInvestigator, CaseInvestigatorAdmin)
