from rest_framework import serializers
from .models import User
from xml.dom import ValidationErr
from django.utils.encoding import smart_str, force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import Util
from .models import User,Document,ProfileDocument

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['name','email','date_of_birth','phone_number','password','bloodgroup','province_number','address','issue']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def create(self, validated_data):
        return User.objects.create_user(** validated_data)
    
    
class UserLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=15)
    class Meta:
        model = User
        fields = ['phone_number', 'password']
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','date_of_birth','phone_number','bloodgroup','province_number','address','issue']
        
        
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','date_of_birth','phone_number','bloodgroup','province_number','address','issue','is_verified']
        
        
class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style= 
    {'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password']
        
    def validate(self, attrs):
        password = attrs.get('password')
        user = self.context.get('user')
        user.set_password(password)
        user.save()
        return attrs
    
    

        
        

        

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Document
        fields='__all__'

class ProfileDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProfileDocument
        fields='__all__'
        
    