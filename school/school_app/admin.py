from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Faculties)
class FacultyAdmin(admin.ModelAdmin):
    pass

@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    pass

@admin.register(Notices)
class NoticeAdmin(admin.ModelAdmin):
    pass

@admin.register(Pictures)
class PictureAdmin(admin.ModelAdmin):
    pass