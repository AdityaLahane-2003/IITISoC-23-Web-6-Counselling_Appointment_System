from django.db import models

# Create your models here.


class form1_data(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_mob_no = models.CharField(max_length=200)
    patient_desiese_symptom = models.CharField(max_length=500)
    date = models.DateField()
    curr_date_time = models.DateTimeField()
    time = models.TimeField()


class form2_data(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_mob_no = models.CharField(max_length=200)
    patient_desiese_symptom = models.CharField(max_length=500)
    date = models.DateField()
    curr_date_time = models.DateTimeField()
    time = models.TimeField()


class form3_data(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_mob_no = models.CharField(max_length=200)
    patient_desiese_symptom = models.CharField(max_length=500)
    date = models.DateField()
    curr_date_time = models.DateTimeField()
    time = models.TimeField()


class form4_data(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_mob_no = models.CharField(max_length=200)
    patient_desiese_symptom = models.CharField(max_length=500)
    date = models.DateField()
    curr_date_time = models.DateTimeField()
    time = models.TimeField()


class form5_data(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_mob_no = models.CharField(max_length=200)
    patient_desiese_symptom = models.CharField(max_length=500)
    date = models.DateField()
    curr_date_time = models.DateTimeField()
    time = models.TimeField()


class form6_data(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_mob_no = models.CharField(max_length=200)
    patient_desiese_symptom = models.CharField(max_length=500)
    date = models.DateField()
    curr_date_time = models.DateTimeField()
    time = models.TimeField()

class contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=12)
    # query = models.TextField()


# This model is for sign-up user data collection during signup and then signin will fetch data from this.


class user_data(models.Model):
    name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
