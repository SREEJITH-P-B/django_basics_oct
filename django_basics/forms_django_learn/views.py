from django.shortcuts import render
from .models import detailss

def home(request):
    return render(request,'forms_django_learn/index.html')
def details(request):
    if request.method=='POST':
        d=detailss()
        d.fname=request.POST.get('fname')
        d.lname=request.POST.get('lname')
        d.stream=request.POST.get('stream')
        d.save()
        context = {
        "fname":d.fname,
        "lname": d.lname,
        "stream": d.stream,
        }
        return render(request,'forms_django_learn/details.html',context)
    else:
        context = {
        "fname":"",
        "lname": "",
        "stream": "",
        }
        return render(request,'forms_django_learn/details.html',context)
