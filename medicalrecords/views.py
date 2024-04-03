from .models import MedicalRecord
from rest_framework import viewsets, permissions
from .serializers import MedicalRecordSerializer

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset=MedicalRecord.objects.all()
    serializer_class=MedicalRecordSerializer
    permission_classes=[permissions.AllowAny]