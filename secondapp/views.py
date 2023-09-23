from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def second(request):
    return HttpResponse('<h1>Hello secondapp</h1>')
def call(request):
    return HttpResponse('<h1>How are you</h1>')
