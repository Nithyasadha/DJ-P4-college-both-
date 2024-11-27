from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ECE(request):
    return HttpResponse('<h1>Electronic communication engineering</h1>')

def EEE(request):
    
    return HttpResponse('<h1>Electrical and electronics engineering</h1>')