from django.utils.timezone import now
from django.db import models

# Create your models here.
class MedicalRecord(models.Model):
    visitSummary=models.CharField(max_length=500)
    prescriptions=models.CharField(max_length=500)
    labWork=models.CharField(max_length=500)
    patientId=models.IntegerField()
    doctorId=models.IntegerField()
    createdDate=models.DateTimeField(default=now())