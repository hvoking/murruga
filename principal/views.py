from django.shortcuts import render
from django.template.response import TemplateResponse


def inspiration(request):
	return TemplateResponse (request, 'hvoking.html', {})



