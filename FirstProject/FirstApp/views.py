from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request , 'FirstApp/index.html')

def home(request):
    return render(request , 'FirstApp/home.html')

def contact(request):
    return render(request , 'FirstApp/contact.html')

