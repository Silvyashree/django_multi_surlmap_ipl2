from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def captain (request):
    return HttpResponse(' <h1> ruturaj </h1>')

def vicecaptian (request):
    return HttpResponse('<h1> vicecaptain of csk </h1>')