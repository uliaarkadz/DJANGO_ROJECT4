from .models import Patient
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class=PatientSerializer
    permission_classes=[permissions.AllowAny]
    
    def get_queryset(self):
        queryset=Patient.objects.all()
        return queryset   

    def retrieve(self,request,pk=None):
        params = pk
        number = params
        records = Patient.objects.filter(doctorId=number)
        serializer = PatientSerializer(records, many = True)
        return Response(serializer.data)