"""
URL configuration for patientsmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from doctors.views import DoctorViewSet
from patients.views import PatientViewSet
from medicalrecords.views import MedicalRecordViewSet

router=routers.DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet, basename="patients")
router.register(r'medicalrecords', MedicalRecordViewSet, basename="medicalrecords")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

