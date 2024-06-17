from django.db import models

class PatientDetailsModel(models.Model):
    GENDER_CHOICES = [('male','Male'),('female','Female'),('others','Others'),]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    address = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

class DoctorDetailsModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()