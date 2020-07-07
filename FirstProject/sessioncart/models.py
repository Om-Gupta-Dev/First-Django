from django.db import models

# Create your models here.

class cart(models.Model):
    item = models.CharField(max_length=30)
    quantity = models.IntegerField()