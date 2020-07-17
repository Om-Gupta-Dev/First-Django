from django.db import models
from django import forms

from django.urls import reverse 

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=30 )
    mail = models.EmailField()
    Message = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail' , kwargs={'pk':self.pk })