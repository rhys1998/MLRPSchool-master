from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, redirect,get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    faculties=Faculties.objects.all()
    notices=Notices.objects.all()
    form = Messageform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("Invalid Credentials")
    args = {'notices': notices, 'faculties': faculties, 'form':form}
    return render(request, 'index.html', args)