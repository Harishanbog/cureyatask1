from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from .models import userdetails
from django.contrib import messages
from django.core.mail import send_mail
from twilio.rest import Client
import random

# Your Account SID from twilio.com/console
account_sid = "AC1b6527f684e9c359e3dcd87c2da597b8"
# Your Auth Token from twilio.com/console
auth_token  = "d06d7ca1242768acdd025c4583826a53"

client = Client(account_sid, auth_token)
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
        mobile_otp=random.randint(0,999999)
        email_otp=random.randint(0,9999)
        user=userdetails.objects.create(firstname=firstname,lastname=lastname,email=email,number=number,type=type,mobile_otp=mobile_otp,email_otp=email_otp)
        user.save()
        Mmess=f"Welcome to cureya Your otp is {mobile_otp}"
        Emess=f"Welcome to cureya Your otp is {email_otp}"
        send_mail('Welcome',Emess,'ss',[email],fail_silently=False)
        message = client.messages.create(
            to="919738113633", 
            from_="+17048692490",
            body=Mmess)
        return render(request,"user/otp_verification.html",{'user':user,'mobile':False})
         
            
           
           
         
def mobile_otp_verification(request):
    userid=request.POST['user']
    otp=request.POST['otp']
    getusr=userdetails.objects.get(id=userid)
    otptype=request.POST.get('otptype')
    if otptype=='mobile':
        if userdetails.objects.filter(id=userid).last().mobile_otp==int(otp):
            messages.success(request,'Mobile number verified succesfully')
            return render(request,"user/otp_verification.html",{'user':getusr,'mobile':True})
        else:
            messages.warning(request,'Wrong otp')
            return render(request,"user/otp_verification.html",{'user':getusr})

    elif otptype=='email':
        if userdetails.objects.filter(id=userid).last().email_otp==int(otp):
            messages.success(request,'Email verified succesfully')
            return HttpResponse("User created successfully and Mobile number and email both aere verified")
        else:
            messages.warning(request,'Wrong otp')
            return render(request,"user/otp_verification.html",{'user':getusr})




 



    

 

