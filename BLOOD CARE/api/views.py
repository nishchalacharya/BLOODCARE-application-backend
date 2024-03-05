from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer,ProfileDocumentSerializer,DocumentSerializer ,UserRegistrationSerializer,UserLoginSerializer, UserProfileSerializer, UserChangePasswordSerializer
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import User,Document,ProfileDocument
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from django.conf import settings

import pyotp
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings





#Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
class UserRegistrationView(APIView):
    #renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token':token,'msg':'Registration Successful'},
        status=status.HTTP_201_CREATED)
        
    
class UserLoginView(APIView):
    #renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.data.get('phone_number')
        password = serializer.data.get('password')
        user = authenticate(phone_number=phone_number, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Phone Number or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
    
    
    
    
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
             

class UserProfileView(APIView):
    # renderer_classes = [UserRenderer]
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk,format=None):
        userdetail=self.get_object(pk)
        serializer = UserProfileSerializer(userdetail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self,request,pk,format=None):
        userupdate=self.get_object(pk)
        serializer =UserProfileSerializer(userupdate,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
    
       
class UserChangePasswordView(APIView):
    # renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data,
        context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)


class SendPasswordResetOTPView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Generate a one-time password (OTP)
        otp_secret_key = pyotp.random_base32()
        otp = pyotp.TOTP(otp_secret_key, interval=180)
        # otp = pyotp.TOTP(otp_secret_key)
        user.password_reset_otp_secret = otp_secret_key
        user.save()

        generated_otp = otp.now()
        print("Generated OTP:", generated_otp)

        # Send the OTP via email
        subject = 'Password Reset OTP'
        message = f'Your OTP for password reset: {generated_otp}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        return Response({'msg': 'Password reset OTP sent successfully'}, status=status.HTTP_200_OK)








# views.py
# views.py
class UserPasswordResetWithOTPView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        otp = request.data.get('otp')
        new_password = request.data.get('new_password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Validate the OTP received from the user
        try:
            totp = pyotp.TOTP(user.password_reset_otp_secret,interval=180)
            generated_otp = totp.now()

            # Ensure that the OTP is valid
            if not totp.verify(otp, valid_window=2):
                raise ValueError(f'Invalid OTP: {otp} vs {generated_otp}')
        except ValueError as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Reset the password
        user.set_password(new_password)
        user.save()

        return Response({'msg': 'Password reset successfully'}, status=status.HTTP_200_OK)

       

















@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def upload_document(request):
 if request.method=='POST'  :
    # Extract user-related information from the request or JWT token

    user_name = request.user.name
    user_id=request.user.id
   

    # Get the uploaded image file from the request data
    documentpic = request.data.get('documentpic')

    if not documentpic:
        return Response({'error': 'No documentpic data provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create a Document instance with the uploaded file
    document = Document.objects.create(
        user_id=user_id,
        name=user_name,  # Assuming you want to use the user's username as the document name
        documentpic=documentpic,
        is_verified=False  # Set to False by default
    )
    
    return Response({'message': 'Document uploaded successfully'})
 
 elif  request.method == 'GET':
      
        # Handling GET request to retrieve user data
        try:
            # Retrieve the user based on the provided pk (user_id)
            user = Document.objects.get(user_id=request.user.id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the user data
        serializer = DocumentSerializer(user)
        return Response(serializer.data)
 else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #  ----------------------------------------------
 

@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def upload_profiledocument(request):
 if request.method=='POST'  :
    # Extract user-related information from the request or JWT token

    user_name = request.user.name
    user_id=request.user.id
   

    # Get the uploaded image file from the request data
    profilepic = request.data.get('profilepic')

    if not profilepic:
        return Response({'error': 'No Profile pic data provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create a Document instance with the uploaded file
    Profilepicture = ProfileDocument.objects.create(
        user_id=user_id,
        name=user_name,  # Assuming you want to use the user's username as the document name
        profilepic=profilepic,
     
     )
    
    return Response({'message': 'Document uploaded successfully'})
 
 elif  request.method == 'GET':
      
        # Handling GET request to retrieve user data
        try:
            # Retrieve the user based on the provided pk (user_id)
            user = ProfileDocument.objects.get(user_id=request.user.id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the user data
        serializer = ProfileDocumentSerializer(user)
        return Response(serializer.data)
 else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 









     




# -------------------------------
# class DocumentViewSet(viewsets.ModelViewSet):
#     queryset = Document.objects.all()
#     serializer_class = DocumentSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

