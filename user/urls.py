from django.urls import path
from .views import home,doctor,mobile_otp_verification

app_name='user'
urlpatterns=[
    path('',home,name="home"),
    path('doctor/',doctor,name="doctor"),
    path('mobile_otp_verification/',mobile_otp_verification,name="mobile_otp_verification"),
]