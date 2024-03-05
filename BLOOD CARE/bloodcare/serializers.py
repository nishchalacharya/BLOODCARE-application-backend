from rest_framework import serializers
from .models import *

class RequestSerializer(serializers.ModelSerializer):
   class Meta:
      model = requestdetails
      fields= ['user_id','user_name','id','pat_name','contact_person','bloodgroup','hospital','req_date','prov_no','district','case_details','phoneno','reqpint','case_details']


class DonorSerializer(serializers.ModelSerializer):
   class Meta:
      model = donordetails
      fields= ['name','gender','phoneno','district','city','dob','prov_no','bloodgrp','confirm','lattitude','longitude']


class imageSerializer(serializers.ModelSerializer):
   class Meta:
      model=profimages
      fields='__all__'



class feedbackSerializer(serializers.ModelSerializer):
   class Meta:
      model = feedback
      fields= '__all__'  

class RewardSerializer(serializers.ModelSerializer):
   class Meta:
      model = reward
      fields = '__all__' 


# class MapSerializer(serializers.ModelSerializer):
#       class Meta:
#          model= Register
#          fields=['id','lattitude','longitude','Name','phoneno']


