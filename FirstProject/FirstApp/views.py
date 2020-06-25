from django.shortcuts import render
import datetime

# Create your views here.

date = datetime.datetime.now()
dt = {'name':'Om Gupta' , 'date':date }

def index(request):
    return render(request , 'FirstApp/index.html' , context = dt)

def home(request):
    return render(request , 'FirstApp/home.html' , context = dt)

def contact(request):
    return render(request , 'FirstApp/contact.html' , context = dt)
    
