from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):
    s='<h1>Hello Django</h1>'
    return HttpResponse(s)

def show(request):
    return HttpResponse('<h1>Hey Everyone</h1>')