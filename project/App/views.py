from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'App/index.html')

def details(request):
    return render(request, 'App/details.html')

def choose_template(request):
    return render(request,'App/choose_template.html')
