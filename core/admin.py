from django.contrib import admin
from .models import *

admin.site.register([Patient, Doctor, Appointment, MedicalRepord, Department])
