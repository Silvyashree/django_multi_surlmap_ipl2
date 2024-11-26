from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captian(request):
    return HttpResponse ('<h1> virat </h1>')