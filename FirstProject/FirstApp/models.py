from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=30)
    mail = models.EmailField()
    Message = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
    