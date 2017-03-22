from django.shortcuts import render
from django.template.response import TemplateResponse


def maps(request):
	return TemplateResponse (request, 'mapa.html', {})

def mapa2(request):
	return TemplateResponse (request, 'mapa2.html', {})