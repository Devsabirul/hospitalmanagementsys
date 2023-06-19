from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    country = models.CharField(max_length=250,null=True,blank=True)
    city = models.CharField(max_length=250,null=True,blank=True)
    state = models.CharField(max_length=250,null=True,blank=True)
    postal_code = models.CharField(max_length=50,null=True,blank=True)
    phone = models.CharField(max_length=50,null=True,blank=True)
    avatar = models.ImageField(upload_to="PatientImage",default="default/user.jpg")
    status = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return str(self.user)

    def age(self):
        today = date.today()
        age = today.year - self.dob.year
        if today.month < self.dob.month or (today.month == self.dob.month and today.day < self.dob.day):
            age -= 1
        return age
    

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    country = models.CharField(max_length=250,null=True,blank=True)
    city = models.CharField(max_length=250,null=True,blank=True)
    state = models.CharField(max_length=250,null=True,blank=True)
    postal_code = models.CharField(max_length=50,null=True,blank=True)
    phone = models.CharField(max_length=50,null=True,blank=True)
    avatar = models.ImageField(upload_to="DoctorImage", default="default/user.jpg")
    short_dio = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return str(self.user.first_name)
    

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
    