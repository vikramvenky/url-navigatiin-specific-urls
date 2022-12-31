from django.shortcuts import render



# Create your views here.

def fun(request):
    dict={'mobile number':[9989132102]}
    return render(request,'venky.html',dict)
