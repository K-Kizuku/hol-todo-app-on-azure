from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Azure')
# Create your views here.