from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('my app1 first view')


# Create your views here.
