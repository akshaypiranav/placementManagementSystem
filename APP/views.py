from django.shortcuts import render
from .models import *

def login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        print(email,password)
        if Student.objects.filter(email=email).exists():
            data=Student.objects.get(email=email)
            if password==data.password:
                return render(request,"home.htm")
    return render(request,"signin.htm")

def register(request):
    if request.method=="POST":
        name=request.POST["name"]
        rollnumber=request.POST["rollnumber"]
        email=request.POST["email"]
        password=request.POST["password"]
        phone=request.POST["mobile"]
        confirm=request.POST["confirm"]
        print(email,password,name,rollnumber,confirm,phone)
        
    return render(request,"signup.htm")

def home(request):
    return render(request,"home.htm")

def drive(request):
    DriveData=Drive.objects.all()
    return render(request,"drive.htm",{"drive":DriveData})


def records(request):
    return render(request,"records.htm")

def passedout(request):
    return render(request,"passedout.htm")

def results(request):
    return render(request,"results.htm")