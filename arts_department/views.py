from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def BCOM(request):
    return HttpResponse('<h1>Bachelor of commerce</h1>')

def BCA(request):
    return HttpResponse('<h1>Bachelor of charted account</h1>')
