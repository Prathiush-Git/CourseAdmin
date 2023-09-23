from django.shortcuts import render
from vazhipadapp.models import vazhitb

# Create your views here.
def aa(request):
        return render(request,'public/layout/base.html')


def add(request):
    if request.method=='POST':
        obj=vazhitb()
        obj.name=request.POST.get('name')
        obj.price=request.POST.get('price')
        obj.save()

    return render(request,'vazhipad/vazhiadd.html')

def vieww(request):
    obj=vazhitb.objects.all()
    return render(request,'vazhipad/vazhiview.html',{'data':obj})

def update(request,pk):
    obj=vazhitb.objects.get(vazhi_id=pk)
    if request.method=='POST':
        obj=vazhitb.objects.get(vazhi_id=pk)
        obj.name=request.POST.get('name')
        obj.price=request.POST.get('price')
        obj.save()
    return render(request,'vazhipad/vazhiupdate.html',{'data':obj})

def delete(request,pk):
    obj=vazhitb.objects.get(vazhi_id=pk)
    obj.delete()
    return vieww(request)