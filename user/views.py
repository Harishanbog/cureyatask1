from django.http.response import HttpResponse
from django.shortcuts import render
from .models import userdetails


# Create your views here.

def home(request):
    if request.method=='POST':
        if request.POST['type']=='doctortype':
           return render(request,"user/doctor.html")
        elif request.POST['type']=='patienttype':
            return render(request,"user/patient.html")   
             
    else:
        return render(request,"user/index.html") 

def doctor(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        number=request.POST['number']
        type=request.POST['type']
        user=userdetails.objects.create(firstname=firstname,lastname=lastname,email=email,number=number,type=type)
        user.save()
        return HttpResponse("User created succesfully")
