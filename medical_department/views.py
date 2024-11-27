from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def MBBS(request):
    return HttpResponse('<h1>Health is wealth</h1>')

def MPHARM(request):
    return HttpResponse('<h1>Medical</h1>')
