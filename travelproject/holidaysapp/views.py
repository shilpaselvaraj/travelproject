from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    x=Team.objects.all()
    return render(request,"index.html",{'result':obj,'teams':x})

# def operation(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,"about.html",{'add':add,'sub':sub,'mul':mul,'div':div})

# def conatct(request):
#     return HttpResponse("hello am contact")