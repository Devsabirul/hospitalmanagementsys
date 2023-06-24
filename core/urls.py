from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('doctors', doctor, name="doctor-list"),
    path('add-doctor', add_doctor, name="add-doctor"),
    path('edit-doctor/<int:id>', edit_doctor, name="edit-doctor"),
    path('patients', patient, name="patient-list"),
    path('appointment', appointment, name="appointment"),
    path('add-appointment', add_appointment, name="add_appointment"),
    path('departments', departments, name="departments"),
    path('add-department', add_department, name="add_department"),
    path('add-patient', add_patient, name="add-patient"),
    path('delete-doctor/<int:id>', delete_doctor, name="delete-doctor"),
    path('delete-patient/<int:id>', delete_patient, name="delete-patient"),
    path('delete-department/<int:id>',
         delete_department, name="delete-department"),
    path('delete-appointment/<int:id>',
         delete_appointment, name="delete-appointment"),
]
