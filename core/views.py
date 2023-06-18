from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
import os
from .models import *

def home(request):
    return render(request,"core/index.html")

def doctor(request):
    doctors = Doctor.objects.order_by("-id")
    return render(request,"core/doctor.html",locals())

def patient(request):
    return render(request,"core/patient.html")


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
        avater = request.FILES.get("avater")
        sort_bio = request.POST.get("sort_bio")
        status = request.POST.get("status")
        User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
        user = User.objects.order_by("-id")[:1].get()
        if avater == None:
            doctor = Doctor(user=user,dob=dob,gender=gender,address=address,country=country,city=city,state=state,postal_code=postal_code,phone=phone,short_dio=sort_bio,status=status)
            doctor.save()
        else:
            doctor = Doctor(user=user,dob=dob,gender=gender,address=address,country=country,city=city,state=state,postal_code=postal_code,phone=phone,avater=avater,short_dio=sort_bio,status=status)
            doctor.save()
        msg = "Doctor added successfully."
    return render(request,"core/add-doctor.html",locals())

def add_patient(request):
    return render(request,"core/add-patient.html")

def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    # Check if the avatar is the default one
    if doctor.avatar != "DoctorImage/default/user_icafoe.jpg":
        # Delete the avatar file from local storage
        if settings.DEFAULT_FILE_STORAGE != 'cloudinary_storage.storage.MediaCloudinaryStorage':
            if doctor.avatar and os.path.isfile(doctor.avatar.path):
                os.remove(doctor.avatar.path)

    # Delete the doctor from the database
    doctor.delete()

    return redirect("doctor-list")
