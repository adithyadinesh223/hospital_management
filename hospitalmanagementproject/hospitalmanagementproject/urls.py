"""
URL configuration for hospitalmanagementproject project.

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
from django.urls import path
from hospitalmanagementapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name='Home'),
    path('PatientRegister',views.PatientRegisterView.as_view(),name='PatientRegister'),
    path('AddDoctor',views.AddDoctorView.as_view(),name='AddDoctor'),
    path('PatientsList',views.ListPatientsView.as_view(),name='PatientsList'),
    path('DoctorsList',views.ListDoctorsView.as_view(),name='DoctorsList'),
    path('PatientDelete/<int:id>',views.PatientDeleteView.as_view(),name='PatientDelete'),
    path('DoctorDelete/<int:id>',views.DoctorDeleteView.as_view(),name='DoctorDelete'),
    path('PatientEdit/<int:id>',views.PatientEditView.as_view(),name='PatientEdit'),
    path('DoctorEdit/<int:id>',views.DoctorEditView.as_view(),name='DoctorEdit'),
]