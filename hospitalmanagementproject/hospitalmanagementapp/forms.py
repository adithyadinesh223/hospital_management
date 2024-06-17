from django import forms
from django.contrib.auth.models import User
from hospitalmanagementapp.models import PatientDetailsModel, DoctorDetailsModel


class PatientRegisterForm(forms.ModelForm):
    class Meta:
        model = PatientDetailsModel
        fields = '__all__'
        widgets = {
                    'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'dob': forms.DateInput(attrs={'type': 'date'}),
                    'gender':forms.Select(attrs={'class':'form-control'}),
                    'address':forms.TextInput(attrs={'class':'form-control'}),
                    'contact_number':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class AddDoctorForm(forms.ModelForm):
    class Meta:
        model = DoctorDetailsModel
        fields = '__all__'
        widgets = {
                    'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'speciality':forms.TextInput(attrs={'class':'form-control'}),
                    'contact_number':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'}),
        }