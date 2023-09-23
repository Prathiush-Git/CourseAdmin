from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greet(request):
    return HttpResponse('<h1>HELLO WELCOME TO HOMEPAGE.</h1>')

def show(request):
    return HttpResponse('<h2>HI THIS IS YOUR CONTACT PAGE.</h2>')

def display(request):
    return HttpResponse('<p1>HERE IS YOUR CONTACT DETAILS</p2>')
