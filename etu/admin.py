from django.contrib import admin
from etu.models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('uid', 'first_name', 'last_name', 'etu', 'alive')
    search_fields = ['uid', 'first_name', 'last_name']

# Register your models here.
admin.site.register(Patient, PatientAdmin)
