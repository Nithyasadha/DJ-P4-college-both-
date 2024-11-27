from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def BSC(request):
    return HttpResponse('<h1>Bachelor of computer science</h1>')

def MSC(request):
    return HttpResponse('<h1>Master of computer science</h1>')
