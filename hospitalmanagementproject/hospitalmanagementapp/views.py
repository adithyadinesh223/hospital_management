from django.shortcuts import render
# Create your views here.
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from hospitalmanagementapp.forms import PatientRegisterForm, AddDoctorForm
from hospitalmanagementapp.models import PatientDetailsModel, DoctorDetailsModel

class HomeView(TemplateView):
    template_name = "home.html"

class PatientRegisterView(CreateView):
    form_class = PatientRegisterForm
    template_name = 'patient_register.html'
    model = PatientDetailsModel
    success_url = reverse_lazy('PatientsList')

class AddDoctorView(CreateView):
    form_class = AddDoctorForm
    template_name = 'add_doctor.html'
    model = DoctorDetailsModel
    success_url = reverse_lazy('DoctorsList')

class ListPatientsView(ListView):
    model = PatientDetailsModel
    template_name = 'patient_list.html'
    context_object_name = "datakey"

class ListDoctorsView(ListView):
    model = DoctorDetailsModel
    template_name = 'doctor_list.html'
    context_object_name = "datakey"

class PatientDeleteView(DeleteView):
    model = PatientDetailsModel
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('PatientsList')
    template_name = 'patient_delete.html'

class DoctorDeleteView(DeleteView):
    model = DoctorDetailsModel
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('DoctorsList')
    template_name = 'doctor_delete.html'

class PatientEditView(UpdateView):
    model = PatientDetailsModel
    form_class = PatientRegisterForm
    template_name = 'patient_edit.html'
    success_url = reverse_lazy('PatientsList')
    pk_url_kwarg = 'id'

class DoctorEditView(UpdateView):
    model = DoctorDetailsModel
    form_class = AddDoctorForm
    template_name = 'doctor_edit.html'
    success_url = reverse_lazy('DoctorsList')
    pk_url_kwarg = 'id'