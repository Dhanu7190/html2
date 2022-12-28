from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('string1 by app1')

def second(request):
    return HttpResponse('string2 by app2')
