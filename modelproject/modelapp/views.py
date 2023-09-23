from django.shortcuts import render
from modelapp.models import modeltb

# Create your views here.
def greet(request):
    if request.method=='POST':
        obj=modeltb()
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.email=request.POST.get('email')
        obj.save()
    return render(request,'web.html')


