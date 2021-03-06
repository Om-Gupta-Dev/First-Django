from django.shortcuts import redirect, render

from CRUD.form import EmpForm
from CRUD.models import Employee

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
        

def Delete_view(request,id):
    emp = Employee.objects.get(id = id)
    emp.delete()
    return redirect('/crud')


def Update_view(request,id):
    emp = Employee.objects.get(id = id)
    if request.method == "POST":
        form = EmpForm(request.POST , instance=emp)       # Creating a form instance and connecting it with emp form to update existing record
        if form.is_valid():
            form.save(commit=True)
            return redirect('/crud')
    if request.method == "GET":
        return render(request , 'CRUD/update.html' , {'employee':emp})
