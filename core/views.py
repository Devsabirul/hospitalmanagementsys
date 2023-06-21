from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
import os
from .models import *
from django.core import serializers
import json


def home(request):
    return render(request, "core/index.html")


def doctor(request):
    doctors = Doctor.objects.order_by("-id")
    return render(request, "core/doctor.html", locals())


def patient(request):
    patients = Patient.objects.order_by("-id")
    return render(request, "core/patient.html", locals())


def appointment(request):
    return render(request, "core/appointments.html", locals())


def serialize_with_related(queryset):
    serialized_data = []
    for obj in queryset:
        serialized_obj = {
            'id': obj.id,
            'user': {
                'id': obj.user.id,
                'first_name': obj.user.first_name,
                'last_name': obj.user.last_name
            }
        }
        serialized_data.append(serialized_obj)

    return json.dumps(serialized_data)


def add_appointment(request):
    patients = Patient.objects.all()
    departments = Department.objects.all()
    appointment_id_ = 1000 if Appointment.objects.count() == 0 else Appointment.objects.aggregate(
        max=Max('appointment_id'))["max"]+1

    try:
        department_id = request.GET.get('department_id')
        doctors = Doctor.objects.filter(
            department_id=department_id).values('id', 'user__first_name', 'user__last_name')
        if doctors:
            return JsonResponse({'doctors': list(doctors)})
    except Exception as e:
        print(e)
    if request.method == "POST":
        appointment_id = request.POST.get('appointment_id')
        patient = request.POST.get('patient')
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        status = request.POST.get('status')

    context = {
        'patients': patients,
        'departments': departments,
        'appointment_id_': appointment_id_
    }
    return render(request, "core/add-appointment.html", context)


def departments(request):
    departments = Department.objects.all()
    return render(request, "core/departments.html", locals())


def add_department(request):
    msg = ""
    doctors = Doctor.objects.all()
    if request.method == "POST":
        department_name = request.POST.get("department_name")
        status = request.POST.get("status")
        department = Department(department_name=department_name, status=status)
        department.save()
        msg = "Department Successfully Added."
    return render(request, "core/add-department.html", locals())


def add_doctor(request):
    msg = ""
    departments = Department.objects.filter(status="Active")
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        department = request.POST.get("department")
        address = request.POST.get("address")
        country = request.POST.get("country")
        city = request.POST.get("city")
        state = request.POST.get("state")
        postal_code = request.POST.get("postal_code")
        phone = request.POST.get("phone")
        avatar = request.FILES.get("avater")
        sort_bio = request.POST.get("sort_bio")
        status = request.POST.get("status")
        user_check = User.objects.filter(username=username).first()
        department_ = Department.objects.get(id=department)
        if user_check:
            msg = "Username already exists."
        else:
            User.objects.create_user(username=username, password=password1,
                                     first_name=first_name, last_name=last_name, email=email)
            user = User.objects.order_by("-id")[:1].get()
            if avatar == None:
                doctor = Doctor(user=user, dob=dob, gender=gender, address=address, country=country, city=city,
                                state=state, postal_code=postal_code, phone=phone, short_dio=sort_bio, status=status, department=department_)
                doctor.save()
            else:
                doctor = Doctor(user=user, dob=dob, gender=gender, address=address, country=country, city=city,
                                state=state, postal_code=postal_code, phone=phone, avatar=avatar, short_dio=sort_bio, status=status, department=department_)
                doctor.save()
            msg = "Doctor added successfully."
    return render(request, "core/add-doctor.html", locals())


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
        user_check = User.objects.filter(username=username).first()
        if user_check:
            msg = "Username already exists."
        else:
            User.objects.create_user(username=username, password=password1,
                                     first_name=first_name, last_name=last_name, email=email)
            user = User.objects.order_by("-id")[:1].get()
            if avatar == None:
                patient = Patient(user=user, dob=dob, gender=gender, address=address, country=country,
                                  city=city, state=state, postal_code=postal_code, phone=phone, status=status)
                patient.save()
            else:
                patient = Patient(user=user, dob=dob, gender=gender, address=address, country=country, city=city,
                                  state=state, postal_code=postal_code, phone=phone, avatar=avatar, short_dio=sort_bio, status=status)
                patient.save()
            msg = "Patient added successfully."
    return render(request, "core/add-patient.html", locals())


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


def delete_department(request, id):
    departments = Department.objects.get(id=id)
    departments.delete()
    return redirect("departments")
