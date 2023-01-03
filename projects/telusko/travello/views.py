from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.
def index(request):

    dest1=Destination()
    dest1.name='mumbai'
    dest1.desc='The city never sleep'
    dest1.price=800
    return render(request,'index.html',{'dest1':dest1});

