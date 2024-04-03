from .models import Doctor
from rest_framework import serializers

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'