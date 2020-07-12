from django.shortcuts import render , redirect
from CRUD.models import Employee
from CRUD.form import EmpForm

# Create your views here.


def home(request):
    employees = Employee.objects.all()
    return render(request , 'CRUD/home.html' , {'employees':employees})


def new(request):
    employees = Employee.objects.all()
    if request.method == "GET":
        form = EmpForm()
        return render(request , 'CRUD/add.html' , {'form':form})
    
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/crud')
        else:
            return render(request , 'CRUD/add.html' , {'form':form})