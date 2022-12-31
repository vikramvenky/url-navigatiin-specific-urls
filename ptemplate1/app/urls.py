from django.urls import path
from app.views import *
app_name='something1'

urlpatterns=[
    path('fun/',fun,name='fun'),
]