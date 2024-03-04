from django.contrib import admin
from django.urls import path, include
from django.conf import settings #for image
from django.conf.urls.static import static #for image

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/user/', include('api.urls')),
    path('bloodcare/',include('bloodcare.urls'))

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
