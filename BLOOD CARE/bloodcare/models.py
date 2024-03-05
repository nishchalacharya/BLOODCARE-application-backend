from django.db import models
from api.models import User

# Create your models here.

class donordetails(models.Model):
    user_id=models.CharField(max_length=10)
    user_name=models.CharField(max_length=100)
    name = models.CharField( max_length=50)
    prov_no = models.CharField( max_length=30)
    district = models.CharField( max_length=50)
    city  = models.CharField( max_length=50)
    bloodgrp=models.CharField(max_length=5)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    # Email = models.EmailField(max_length=100)
    # GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    # )
    gender = models.CharField(max_length=20)  #choices=GENDER_CHOICES
    phoneno = models.CharField(max_length=10,unique=False)
    confirm =  models.BooleanField(default=False)
    lattitude=models.CharField(max_length=20)
    longitude=models.CharField(max_length=20)


class requestdetails (models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id=models.CharField(max_length=10)
    user_name=models.CharField(max_length=100)
    pat_name = models.CharField( max_length=50)
    contact_person = models.CharField(max_length=50)
    bloodgroup = models.CharField(max_length=10)
    prov_no = models.CharField( max_length=2)
    district = models.CharField( max_length=50)
    hospital= models.CharField(max_length=75)
    reqpint = models.IntegerField(default=1)
    phoneno = models.CharField(max_length=10,unique=False)
    req_date = models.DateField( auto_now=False, auto_now_add=False)
    case_details = models.CharField(max_length=150)



class feedback(models.Model):
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    emailid = models.EmailField( max_length=254)
    phoneno = models.CharField(max_length=10)


class profimages(models.Model):
    profilepic=models.ImageField(upload_to='profile_pictures')
    


class reward(models.Model):
    reward_point = models.IntegerField(default=0.0)



