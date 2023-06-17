from django.urls import path 
from .views import *
urlpatterns = [
    path('',home,name="home"),
    path('doctors',doctor,name="doctor-list"),
    path('add-doctor',add_doctor,name="add-doctor"),
    path('patients',patient,name="patient-list"),
    path('add-patient',add_patient,name="add-patient"),
]
