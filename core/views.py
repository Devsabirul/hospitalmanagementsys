from django.shortcuts import render

def home(request):
    return render(request,"core/index.html")

def doctor(request):
    return render(request,"core/doctor.html")