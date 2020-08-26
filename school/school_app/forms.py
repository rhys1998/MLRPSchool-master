from django import forms
from .models import *


class Messageform(forms.ModelForm):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    content = models.TextField()

    class Meta:
        model = Messages
        fields = ('name', 'email', 'mobile', 'content',)