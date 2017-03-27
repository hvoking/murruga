from django.shortcuts import render
from django.template.response import TemplateResponse


def particles(request):
	return TemplateResponse (request, 'particles.html', {})