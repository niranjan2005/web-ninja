from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dest1 = Destination.objects.all()
    dest1 = Destination()
    dest1.name = 'World Tour'
    dest1.desc = 'CEO of this webpage is T.Niranjan'
    dest1.logo = 'logo.png'
    dest1.Nickname = 'Ninja Tech'
    dest1.release = '13 Days To Go'
    dest1.name1 = True
    dest1.Nickname1 = True
    dest1.desc1 = True
    dest1.release1 = True
    dest1.logo1 = True

    return render(request, "index.html", {'dest1': dest1})
