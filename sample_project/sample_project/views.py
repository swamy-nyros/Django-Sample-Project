from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    response = TemplateResponse(request, 'sample_project/home.html')    
    return response
