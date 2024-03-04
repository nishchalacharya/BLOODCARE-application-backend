from django.contrib import admin
from django.urls import path,include
from rest_framework. routers import DefaultRouter
from .views import (
    bloodrequest_list,  feedbackviewset, DonorDetail,requestviewset,imagedetail,request_detail
    
)
from rest_framework import views
# request_detail
router=DefaultRouter()

router.register(r'requests',requestviewset, basename='request_detail'),
router.register(r'donors', DonorDetail, basename='donor')  # Explicit basename
# router.register(r'profiles', ProfileViewset, basename='profile')
# router.register(r'locations',Locationviewset, basename='location')
router.register(r'images',imagedetail,basename='images')

# urlpatterns=router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('feedback/',feedbackviewset, name='feedback-list'),  # Clear purpose and name
    path('req-detail/<int:pk>/',request_detail,name='request-detail'),
    path('bloodreqlst/',bloodrequest_list),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
    
]

