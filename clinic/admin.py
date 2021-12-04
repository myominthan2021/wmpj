from django.contrib import admin
from .models import Clinic
# Register your models here.


class ClinicAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'patient_phone', 'patient_address', 'patient_case', 'fileupload', 'drug', 'fees', 'datetime', 'doctor']
    list_filter = ['patient_name', 'patient_phone', 'patient_address', 'patient_case', 'fileupload', 'drug', 'fees', 'datetime', 'doctor']
    search_fields = ['patient_name']

admin.site.register(Clinic, ClinicAdmin)