from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your models here.


def content_file_name(instance,filename):
	ext="png"
	filename= str(instance.name)+"."+str(ext)
	return os.path.join('images/',filename)

class Faculties(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    url_Facebook = models.URLField()
    url_Instagram = models.URLField()
    url_Twitter = models.URLField()
    image = models.ImageField(upload_to=content_file_name)
    # TODO
    # AUTOGENERATE DATETIME
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def get_cname(self):
        class_name = "Faculty"
        return class_name

    class Meta:
        managed = True
        ordering = ['-created_at']
        db_table = 'faculties'
        verbose_name_plural = 'Faculties'


class Messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'messages'
        verbose_name_plural = 'Messages'
    def __self__(self):
        return self.name

class Notices(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'notices'
        verbose_name_plural = 'Notices'
    def __self__(self):
        return self.title