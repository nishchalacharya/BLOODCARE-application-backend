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

# Create your views here.


class DonorDetail(viewsets.ModelViewSet):
    queryset=donordetails.objects.all()
    serializer_class= DonorSerializer
    filter_backends=[SearchFilter]
    search_fields=['^city','^hospital']

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
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
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
        bloodreq =requestdetails.objects.all()
        serializer=RequestSerializer(bloodreq,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','POST','DELETE'])
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
        

        