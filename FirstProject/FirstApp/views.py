from django.shortcuts import render

# Create your views here.

def index(request):
    dt = {'name':'Om Gupta'}
    return render(request , 'FirstApp/index.html' , context = dt)

def home(request):
    return render(request , 'FirstApp/home.html')

def contact(request):
    return render(request , 'FirstApp/contact.html')

