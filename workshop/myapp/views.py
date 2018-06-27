from django.shortcuts import render
from .models import Workshop

# Create your views here.

def index(request):
    workshops = Workshop.objects.all()
    context ={'workshop':workshops}
    return render(request,'myapp/index.html',context)

def detail(request):
    workshops = Workshop.objects.all()
    context = {'workshop': workshops}
    return render(request,'myapp/base.html',context)
