from .models import MedicalRecord
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import MedicalRecordSerializer

class MedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class=MedicalRecordSerializer
    permission_classes=[permissions.AllowAny]
    
    def get_queryset(self):
        queryset=MedicalRecord.objects.all()
        return queryset
    
    def retrieve(self,request,pk=None):
        params = pk
        number = params
        records = MedicalRecord.objects.filter(patientId=number)
        serializer = MedicalRecordSerializer(records, many = True)
        return Response(serializer.data)