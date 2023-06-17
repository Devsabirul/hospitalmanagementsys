from django.shortcuts import render

def home(request):
    return render(request,"core/index.html")

def doctor(request):
    return render(request,"core/doctor.html")

def patient(request):
    return render(request,"core/patient.html")


def add_doctor(request):
    return render(request,"core/add-doctor.html")

def add_patient(request):
    return render(request,"core/add-patient.html")