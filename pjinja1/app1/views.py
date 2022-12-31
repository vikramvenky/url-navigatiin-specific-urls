from django.shortcuts import render

# Create your views here.
 

def jinja(request):
    d={'name':'vikram'}
    return render(request,'first.html',d)
