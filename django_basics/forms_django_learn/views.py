from django.shortcuts import render
def home(request):
    return render(request,'forms_django_learn/index.html')
def details(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        stream=request.POST.get('stream')
        context = {
        "fname":fname,
        "lname": lname,
        "stream": stream,
        }
        return render(request,'forms_django_learn/details.html',context)
    else:
        context = {
        "fname":"",
        "lname": "",
        "stream": "",
        }
        return render(request,'forms_django_learn/details.html',context)
