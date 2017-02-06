from django.shortcuts import render
from django.http import HttpResponse
from .models import Oferta

def index(request):
    return HttpResponse('index')

def get_oferta(request, slug):
    oferta = Oferta.objects.get(slug=slug).content
    response = HttpResponse(oferta)
    response['x-frame-options'] = 'SAMEORIGIN'
    return response
