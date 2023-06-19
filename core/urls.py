from django.urls import path 
from .views import *
urlpatterns = [
    path('',home,name="home"),
    path('doctors',doctor,name="doctor-list"),
    path('add-doctor',add_doctor,name="add-doctor"),
    path('patients',patient,name="patient-list"),
    path('add-patient',add_patient,name="add-patient"),
    path('delete-doctor/<int:id>',delete_doctor,name="delete-doctor"),
    path('delete-patient/<int:id>',delete_patient,name="delete-patient"),
]
