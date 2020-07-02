from django import forms
from django.core import validators

def only_gmail(value):
    if value[-10:] != "@gmail.com":
        raise forms.ValidationError("mail should be Only Gmail..")
        
def only_alpha(value):
    if value.isalpha() != True:
        raise forms.ValidationError("Name should Only Contain Alphabets..")
    
class MessageSend(forms.Form):
    name = forms.CharField(validators=[only_alpha , validators.MinLengthValidator(5)])
    mail = forms.EmailField(validators = [only_gmail])
    Message = forms.CharField(widget=forms.Textarea , validators=[validators.MaxLengthValidator(200) , validators.MinLengthValidator(10)])
    date = forms.DateField()