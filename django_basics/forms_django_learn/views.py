from django.shortcuts import render,redirect
from .models import detailss

def home(request):
    return render(request,'forms_django_learn/index.html')
def details(request):
    if request.method=='POST':
        d=detailss()
        d.fname=request.POST.get('fname')
        d.lname=request.POST.get('lname')
        d.stream=request.POST.get('stream')
        d.completed=0
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
def show(request):
        query_results = detailss.objects.all()
        context ={
            "results":query_results,
        }
        return render(request,'forms_django_learn/show.html',context)

def display_row(request):
        if request.method=='POST':
            query_results = detailss.objects.filter(stream=request.POST.get('stream'))
            context ={
                "results":query_results
            }
            return render(request,'forms_django_learn/row.html',context)
        else:
            return render(request,'forms_django_learn/row.html')

def completed_item(request,ids):
    results=detailss.objects.get(pk=ids)
    if(results.completed==True):
            results.completed=False;
            results.save()
    else:
            results.completed=True;
            results.save()
    return redirect('show')