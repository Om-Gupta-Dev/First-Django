from django import forms

from CRUD import models 

class EmpForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = '__all__'
        