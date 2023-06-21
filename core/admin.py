from django.contrib import admin
from .models import *


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'appointment_date', 'time')


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register([Patient, Doctor,  MedicalRepord, Department])
