from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    contact_num = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField( max_length=254)
    insurance_details = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    contact_num = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    departments = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.doctor),str(self.patient),str(self.appointment_date)
    

class MedicalRepord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.CharField( max_length=100)
    prescription = models.TextField()
    treatment = models.CharField( max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.treatment
    

class Department(models.Model):
    department_name = models.CharField(max_length=50)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name
    