from django.contrib import admin
from .models import *

# # Register your models here.
@admin.register(donordetails)
class DonorDetailsAdmin(admin.ModelAdmin):
    list_display=['name','prov_no','district','city','dob','gender','phoneno']


@admin.register(requestdetails)
class RequestDetails(admin.ModelAdmin):
     list_display=['pat_name','contact_person','bloodgroup','district','hospital','req_date']


admin.site.register(reward)


@admin.register(profimages)
class ProfileImages(admin.ModelAdmin):
     list_display=['id','profilepic']



@admin.register(feedback)
class Feedback(admin.ModelAdmin):
     list_display=['name','message','phoneno','emailid']