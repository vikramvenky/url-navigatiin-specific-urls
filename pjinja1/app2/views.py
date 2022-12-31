from django.shortcuts import render
from app2.views import *

# Create your views here.

def jinja_(request):
    dict={'number':[9989132102]}

    return render(request,'second.html',dict)
    