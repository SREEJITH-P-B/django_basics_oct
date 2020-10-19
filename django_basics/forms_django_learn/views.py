from django.shortcuts import render
def home(request):
    return render(request,'forms_django_learn/index.html')
def details(request):
    return render(request,'forms_django_learn/details.html')
