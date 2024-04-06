from .models import MedicalRecord
from rest_framework import serializers

class MedicalRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=MedicalRecord
        fields=("visitSummary","prescriptions", "labWork", "patientId", "createdDate", "id")
        