from django.db import models
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
choice=(
    ('D','doctor'),
    ('P','patient')
)
class userdetails(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=10)
    email=models.EmailField()
    number=models.BigIntegerField()
    type=models.CharField(choices=choice,max_length=10)