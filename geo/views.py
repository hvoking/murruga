from django.shortcuts import render
from django.template.response import TemplateResponse


def maps(request):
	return TemplateResponse (request, 'mapa.html', {})