from django.shortcuts import render
from rest_framework import viewsets
from rest_framework .response import Response
from rest_framework import status
from rest_framework.authentication import  SessionAuthentication,BasicAuthentication
from rest_framework.permissions import DjangoModelPermissions,IsAuthenticated,IsAdminUser
from rest_framework.decorators import api_view,APIView,authentication_classes,permission_classes
from .models import *
from .serializers import *
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter
from api.models import User

# Create your views here.


class DonorDetail(viewsets.ModelViewSet):
    queryset=donordetails.objects.all()
    serializer_class= DonorSerializer
    filter_backends=[SearchFilter]
    search_fields=['^city','^hospital','^bloodgrp']

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[DjangoModelPermissions]




class imagedetail(viewsets.ModelViewSet):
    queryset=profimages.objects.all()
    serializer_class=imageSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
   


# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])

@api_view(['POST','GET'])
def feedbackviewset(request):
 
 if request.method=='POST':
    serializer=RequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg':'Thank you for your feedback','status':'success','message':serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
 elif request.method=='GET':
        feedbackdetail= feedback.objects.all()
        serializer=feedbackSerializer(feedbackdetail,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    



# class Locationviewset(viewsets.ModelViewSet):
#     queryset = Register.objects.all()
#     serializer_class=MapSerializer
#     authentication_classes=[BasicAuthentication]
#     permission_classes=[IsAuthenticated]



class requestviewset(viewsets.ModelViewSet):
    queryset = requestdetails.objects.all()
    serializer_class= RequestSerializer
    filter_backends=[SearchFilter]
    search_fields=['^district','^hospital']
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# @permission_classes([DjangoModelPermissions])    
    

@api_view(['GET','POST','DELETE','PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def bloodrequest_list(request):
    queryset = requestdetails.objects.all() 
    # list all requester details ,or create a new details
    if request.method =='GET':
        bloodreq =requestdetails.objects.filter(user=request.user.id)
        serializer=RequestSerializer(bloodreq,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','POST','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def  request_detail(request,pk):
    # Retrieve,update or delete  a blood request details  
     try:
        bloodrequest_detail=requestdetails.objects.get(pk=pk)
     except requestdetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   

     if request.method=='GET':
            serializer=RequestSerializer(bloodrequest_detail)
            return Response(serializer.data)
        
     elif request.method =='DELETE' :
            bloodrequest_detail.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
     

# -------------------------------request detail-----------------
     

@api_view(['POST','GET','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def requestblood(request):
 if request.method=='POST'  :
    # Extract user-related information from the request or JWT token

    user_name = request.user.name
    user_id=request.user.id

    pat_name=request.data.get('pat_name')
    contact_person=request.data.get('contact_person')
    bloodgroup=request.data.get('bloodgroup')
    prov_no=request.data.get('prov_no')
    district=request.data.get('district')
    hospital=request.data.get('hospital')
    reqpint=request.data.get('reqpint')
    phoneno=request.data.get('phoneno')
    req_date=request.data.get('req_date')
    case_details=request.data.get('case_details')


    if not pat_name:
        return Response({'error': 'No patient name provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create a Document instance with the uploaded file
    bloodrequestdetail = requestdetails.objects.create(
       
        user_id=user_id,
        user_name=user_name,  # Assuming you want to use the user's username as the document name
        pat_name=pat_name,
        contact_person=contact_person,
        bloodgroup=bloodgroup,
        prov_no=prov_no,
        district=district,
        hospital=hospital,
        reqpint=reqpint,
        phoneno=phoneno,
        req_date=req_date,
        case_details=case_details
        )
    
    return Response({'message': 'Details received successfully'})
 
 elif  request.method == 'GET':
      
        # Handling GET request to retrieve user data
        try:
            # Retrieve the user based on the provided pk (user_id)
            user = requestdetails.objects.filter(user_id=request.user.id)
        except User.DoesNotExist:
            return Response({'error': 'Details  not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the user data
        serializer = RequestSerializer(user,many=True)
        return Response(serializer.data)
 elif request.method=='DELETE':
        try:
            document_to_delete=requestdetails.objects.filter(user_id=request.user.id)
            document_to_delete.delete()
            return Response({'message':'Request Deleted Successfully'})
        except requestdetails.DoesNotExist:
            return Response({'error':'Request not found'},status=status.HTTP_404_NOT_FOUND)
        
        
 else:  
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)     
     
        

        