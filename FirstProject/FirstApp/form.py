from django import forms
from django.core import validators
from FirstApp import models
from django.contrib.auth.models import User

def only_gmail(value):
    print("validating mail in def")
    if value[-10:] != "@gmail.com":
        raise forms.ValidationError("mail should be Only Gmail..")
        
# def only_alpha(value):
#     print("validating al in def")
#     if value.isalpha() == 'False':
#         raise forms.ValidationError("Name should Only Contain Alphabets..")
        
# def bot_handler(value):
#     print(value)
#     if len(value) > 0:
#         raise forms.ValidationError("Thanks Bot")
    
    
class MessageSend(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = '__all__'
        widgets = {
            'name': forms.TextInput
                           (attrs={'class':'btn btn-outline-warning fields col-md-10 col-sm-10 col-lg-10 col-xs-10', 'id':'enter'}),
            'mail': forms.TextInput
                           (attrs={'class':'btn btn-outline-warning fields col-md-10 col-sm-10 col-lg-10 col-xs-10', 'id':'enter'}),
            'Message': forms.TextInput
                           (attrs={'class':'btn btn-outline-warning fields col-md-10 col-sm-10 col-lg-10 col-xs-10', 'id':'enter'}),
            'date': forms.TextInput
                           (attrs={'class':'btn btn-outline-warning fields col-md-10 col-sm-10 col-lg-10 col-xs-10', 'id':'enter'}),            
        }
        validators = {
            'mail':[only_gmail]
        }
    
    
    # name = forms.CharField(validators=[only_alpha , validators.MinLengthValidator(5)])
    # mail = forms.EmailField(validators=[only_gmail])
    # Message = forms.CharField(widget=forms.Textarea , validators=[validators.MaxLengthValidator(200) , validators.MinLengthValidator(10)])
    # password = forms.CharField(label = "Passsword(Again)" , widget = forms.PasswordInput)
    # rpassword = forms.CharField(widget = forms.PasswordInput)
    # date = forms.DateField()
    # bot_handler = forms.CharField(required = False , widget = forms.HiddenInput , validators = [bot_handler])
        
    
class signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'username' , 'password' , 'email' ]