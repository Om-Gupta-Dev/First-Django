from django.db import models

# Create your models here.

class Employee(models.Model):
    eNo = models.IntegerField()
    eName = models.CharField(max_length=64)
    eSalary = models.IntegerField()
    eAddress = models.CharField(max_length=256)