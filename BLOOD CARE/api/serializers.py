from rest_framework import serializers
from .models import User,Document
from xml.dom import ValidationErr
from django.utils.encoding import smart_str, force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import Util

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
        fields = ['id','name','email','date_of_birth','phone_number','bloodgroup','province_number','address','issue']
        
        
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
    
    
class SendPasswordResetEmailSerializer(serializers.Serializer):
    email= serializers.EmailField(max_length=255)
    class Meta:
        fields = ['email']
        
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded uid', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)
            link = 'http://localhost:3000/api/user/reset/'+uid+'/'+token
            print('Password Reset Link', link)
            #Send Email
            body = 'Click Following Link to Reset Your Password' +link
            data = {
                'subject':'Reset Your Password',
                'body':body,
                'to_email':user.email
            }
            #Util.send_email(data)
            return attrs
        else:
            raise ValidationErr('You are not a Registered User')
        
class UserPasswordResetViewSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password']
        
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            uid = self.context.get('uid')
            token = self.context.get('token')
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise serializers.ValidationError('Token is not valid or Expired')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)
            raise serializers.ValidationError('Token is not Valid or Expired')
        

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Document
        fields='__all__'
        
    