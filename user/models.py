from django.db import models
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
 
class userdetails(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=10)
    email=models.EmailField()
    number=models.BigIntegerField()
    type=models.CharField(max_length=10)
    mobile_otp=models.IntegerField(default=0)
    email_otp=models.IntegerField(default=0)


    def __str__(self):
        return f"{self.firstname} {self.type}"