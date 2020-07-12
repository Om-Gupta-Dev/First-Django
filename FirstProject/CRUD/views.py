from django.shortcuts import render
from CRUD.models import Employee

# Create your views here.


def home(request):
    employees = Employee.objects.all()
    return render(request , 'CRUD/home.html' , {'employees':employees})