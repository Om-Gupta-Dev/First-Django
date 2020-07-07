from django.contrib import admin
from sessioncart import models

class CartAdmin(admin.ModelAdmin):
    list_display = ['item' , 'quantity']

# Register your models here.

admin.site.register(models.cart , CartAdmin)