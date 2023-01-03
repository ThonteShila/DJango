from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city never sleep'
    dest1.img = 'destination_1.jpg'
    dest1.price = 800

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'Hyderabad biryanii is awaysome'
    dest2.img = 'destination_2.jpg'
    dest2.price = 400

    dest3 = Destination()
    dest3.name = 'Pune'
    dest3.desc = 'Nice city'
    dest3.img = 'destination_3.jpg'
    dest3.price = 1100

    dests =[dest1,dest2,dest3]
    return render(request, 'index.html', {'dests': dests})
