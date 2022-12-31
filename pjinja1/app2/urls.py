from django.urls import path
from app2.views import*

urlpatterns=[
    path('jinja_/',jinja_,name='jinja_')
]