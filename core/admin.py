from django.contrib import admin
from models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display = ('uid', 'first_name', 'last_name', 'etu')
    search_fields = ['uid', 'first_name', 'last_name']

# Register your models here.
admin.site.register(Patient, PatientAdmin)
