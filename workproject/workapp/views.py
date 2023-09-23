from django.shortcuts import render
from workapp.models import register

def display(request):
    return render(request,'home.html')

def show(request):
    return render(request,'login.html')

def regist(request):
    if request.method=='POST':
        obj=register()
        obj.name=request.POST.get("name")
        obj.address=request.POST.get("address")
        obj.email=request.POST.get("email")
        obj.password=request.POST.get("password")
        obj.save()
        

    return render(request,'register.html')