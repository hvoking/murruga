from django.shortcuts import render
from django.template.response import TemplateResponse


def mapa2(request):
	return TemplateResponse (request, 'mapa2.html', {})

def mapa3d(request):
	return TemplateResponse (request, 'mapa3d.html', {})

def mapa4d(request):
	return TemplateResponse (request, 'mapa4d.html', {})	