from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer,DocumentSerializer ,UserRegistrationSerializer,UserLoginSerializer, UserProfileSerializer, UserChangePasswordSerializer, SendPasswordResetEmailSerializer,UserPasswordResetViewSerializer
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import User,Document
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from rest_framework.decorators import api_view,authentication_classes,permission_classes




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
        
    
            
class SendPasswordResetEmailView(APIView):
    def post(self,request,format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Reset link send. Please Check your Email'},status=status.HTTP_200_OK)
       
    
class UserPasswordResetView(APIView):
    def post(self, request,uid,token,format=None):
        serializer = UserPasswordResetViewSerializer(data=request.data,
        context={'uid':uid,'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Reset Successfully'},
            status=status.HTTP_200_OK)
       


# class DocumentView(viewsets.ModelViewSet):
#     queryset=Document.objects.all()
#     serializer_class=DocumentSerializer


# import base64  
# from django.core.files.base import ContentFile  


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
        isverified=False  # Set to False by default
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










     




# -------------------------------
# class DocumentViewSet(viewsets.ModelViewSet):
#     queryset = Document.objects.all()
#     serializer_class = DocumentSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

