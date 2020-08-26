from django.urls import path
from .views import *
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name="index"),
    path('gallery',gallery,name="gallery")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   