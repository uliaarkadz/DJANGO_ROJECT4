from django.utils.timezone import now
from django.db import models

# Create your models here.
class Patient(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    doctorId=models.IntegerField()
    createdDate=models.DateTimeField(default=now())