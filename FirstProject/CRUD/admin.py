from django.contrib import admin

from CRUD import models

class EmpAdmin(admin.ModelAdmin):
    list_display = ['eNo' , 'eName' , 'eSalary' , 'eAddress']


# Register your models here.

admin.site.register(models.Employee , EmpAdmin)