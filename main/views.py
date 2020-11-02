from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def index(request):
    template = loader.get_template('main/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def cervezas(request):
    template = loader.get_template('main/cervezas.html')
    context = {}
    return HttpResponse(template.render(context, request))

def registro(request):
    template = loader.get_template('main/registro.html')
    context ={}
    return HttpResponse(template.render(context, request))






