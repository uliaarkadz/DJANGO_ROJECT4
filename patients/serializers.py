from .models import Patient
from rest_framework import serializers

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Patient
        fields=("id","firstName","lastName", "dob", "gender", "status","doctorId","createdDate")