from django.shortcuts import render
from templeapp.models import temptb

# Create your views here.

def add(request):
    if request.method=='POST':
        obj=temptb()
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.time=request.POST.get('time')
        obj.contact=request.POST.get('contact')
        obj.save()
    
    return render(request,'public/tempadd.html')

def vieww(request):
    obj=temptb.objects.all()
    return render(request,'temple/tempview.html',{'data':obj})

def update(request,pk):
    obj=temptb.objects.get(temp_id=pk)
    if request.method=='POST':
        obj=temptb.objects.get(temp_id=pk)
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.time=request.POST.get('time')
        obj.contact=request.POST.get('contact')
        obj.save()
    return render(request,'temple/tempupdate.html',{'data':obj})

def delete(request,pk):
    obj=temptb.objects.get(temp_id=pk)
    obj.delete()
    return vieww(request)
