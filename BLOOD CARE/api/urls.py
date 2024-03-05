from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, upload_profiledocument,UserLoginView, upload_document,UserProfileView, UserChangePasswordView, UserList, UserDetail, SendPasswordResetEmailView, UserPasswordResetView
# from rest_framework_simplejwt import TokenObtainPairView, TokenRefreshView

#upload_document

# router=DefaultRouter()
# router.register(r'documents',DocumentViewSet, basename='document_detail')

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('',include(router.urls)),

    path("profilepictures/",upload_profiledocument,name='upload  profile document'),
    path("documents/",upload_document,name='upload document'),
    path("register/", UserRegistrationView.as_view(), name='register'),
    path("login/", UserLoginView.as_view(), name='login'),
    path("profile/<int:pk>/", UserProfileView.as_view(), name='profile'),
    path("changepassword/", UserChangePasswordView.as_view(), name='changepassword'),
    path("list/",  UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(),name='reset-password'),
]
