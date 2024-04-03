from .models import Doctor
from rest_framework import viewsets, permissions
from .serializers import DoctorSerializer



class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    permission_classes=[permissions.AllowAny]