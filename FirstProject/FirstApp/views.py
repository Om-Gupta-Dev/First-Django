from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    date = datetime.datetime.now()
    dt = {'name':'Om Gupta' , 'date':date }
    return render(request , 'FirstApp/index.html' , context = dt)

def home(request):
    return render(request , 'FirstApp/home.html')

def contact(request):
    return render(request , 'FirstApp/contact.html')

