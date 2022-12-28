from django.urls import path
from app1.views import *
app_name='any1'
urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]