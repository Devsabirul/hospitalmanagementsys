from django.shortcuts import render,redirect
from django.contrib.auth.models import User
import os
from .models import *

def home(request):
    return render(request,"core/index.html")

def doctor(request):
    doctors = Doctor.objects.order_by("-id")
    return render(request,"core/doctor.html",locals())

def patient(request):
    patients = Patient.objects.order_by("-id")
    return render(request,"core/patient.html",locals())


def add_doctor(request):
    msg = ""
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        country = request.POST.get("country")
        city = request.POST.get("city")
        state = request.POST.get("state")
        postal_code = request.POST.get("postal_code")
        phone = request.POST.get("phone")
        avatar = request.FILES.get("avater")
        sort_bio = request.POST.get("sort_bio")
        status = request.POST.get("status")
        User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
        user = User.objects.order_by("-id")[:1].get()
        if avatar == None:
            doctor = Doctor(user=user,dob=dob,gender=gender,address=address,country=country,city=city,state=state,postal_code=postal_code,phone=phone,short_dio=sort_bio,status=status)
            doctor.save()
        else:
            doctor = Doctor(user=user,dob=dob,gender=gender,address=address,country=country,city=city,state=state,postal_code=postal_code,phone=phone,avatar=avatar,short_dio=sort_bio,status=status)
            doctor.save()
        msg = "Doctor added successfully."
    return render(request,"core/add-doctor.html",locals())

def add_patient(request):
    msg = ""
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        country = request.POST.get("country")
        city = request.POST.get("city")
        state = request.POST.get("state")
        postal_code = request.POST.get("postal_code")
        phone = request.POST.get("phone")
        avatar = request.FILES.get("avater")
        status = request.POST.get("status")
        User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
        user = User.objects.order_by("-id")[:1].get()
        if avatar == None:
            patient = Patient(user=user,dob=dob,gender=gender,address=address,country=country,city=city,state=state,postal_code=postal_code,phone=phone,status=status)
            patient.save()
        else:
            patient = Patient(user=user,dob=dob,gender=gender,address=address,country=country,city=city,state=state,postal_code=postal_code,phone=phone,avatar=avatar,short_dio=sort_bio,status=status)
            patient.save()
        msg = "Patient added successfully."
    return render(request,"core/add-patient.html")

def delete_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    if doctor.avatar != "default/user.jpg":
        os.remove(doctor.avatar.path)
        doctor.delete()
    else:
        doctor.delete()
    return redirect("doctor-list")

def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    if patient.avatar != "default/user.jpg":
        os.remove(patient.avatar.path)
        patient.delete()
    else:
        patient.delete()
    return redirect("patient-list")
