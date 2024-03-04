from django.contrib import admin
from .models import User,Document
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
  # The fields to be used in displaying the User model.
  # These override the definitions on the base UserModelAdmin
  # that reference specific fields on auth.User.
  
  list_display = ('id','name','email','date_of_birth','phone_number','bloodgroup','province_number','address','issue','is_admin','is_active')
  list_filter = ('is_admin','is_active',)
  fieldsets = (
      ('User Credentials', {'fields': ('phone_number', 'password')}),
      ('Personal info', {'fields': ('name', 'email', 'date_of_birth','bloodgroup','province_number','address','issue')}),
      ('Permissions', {'fields': ('is_admin','is_active',)}),
 
  )
  # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
  # overrides get_fieldsets to use this attribute when creating a user.
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('phone_number','name','email','date_of_birth','bloodgroup','province_number','address','issue','password'),
      }),
  )
  search_fields = ('phone_number',)
  ordering = ('phone_number', 'id')
  filter_horizontal = ()


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)


# @admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
     list_display=['user_id','name','isverified']

    #  def user_phoneno(self,obj):
    #      return obj.user.phone_number

    #  def name(self,obj):
    #      return obj.user.name
     

admin.site.register(Document, DocumentAdmin)     