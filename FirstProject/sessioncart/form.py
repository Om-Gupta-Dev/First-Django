from django import forms
from django.core import validators
from sessioncart import models
    
class cartForm(forms.ModelForm):
    class Meta:
        model = models.cart
        fields = '__all__'