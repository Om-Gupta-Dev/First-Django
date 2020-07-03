from django import forms
from django.core import validators

def only_gmail(value):
    print("validating mail in def")
    if value[-10:] != "@gmail.com":
        raise forms.ValidationError("mail should be Only Gmail..")
        
def only_alpha(value):
    print("validating al in def")
    if value.isalpha() == 'False':
        raise forms.ValidationError("Name should Only Contain Alphabets..")
        
def bot_handler(value):
    print(value)
    if len(value) > 0:
        raise forms.ValidationError("Thanks Bot")
    
    
class MessageSend(forms.Form):
    name = forms.CharField(validators=[only_alpha , validators.MinLengthValidator(5)])
    mail = forms.EmailField(validators=[only_gmail])
    Message = forms.CharField(widget=forms.Textarea , validators=[validators.MaxLengthValidator(200) , validators.MinLengthValidator(10)])
    password = forms.CharField(label = "Passsword(Again)" , widget = forms.PasswordInput)
    rpassword = forms.CharField(widget = forms.PasswordInput)
    date = forms.DateField()
    bot_handler = forms.CharField(required = False , widget = forms.HiddenInput , validators = [bot_handler])
        
    
        
    # def clean(self):
    #     xx = self.cleaned_data
    #     print("---------------------------/n/n",xx)
        
    #     cleaned_data = super().clean()
    #     print(cleaned_data)
        
    #     inputName = xx['name']
    #     print(inputName)
    #     inputMail = xx['mail']
    #     inputPwd = xx['password']
    #     inputRPwd = xx['rpassword']
        
    #     # if inputName.isalpha() == False :
    #     #     raise forms.ValidationError("Name should Only Contain Alphabets")
    #     if inputMail[-10:] != "@gmail.com":
    #         print("validating mail in Clean")
    #         raise forms.ValidationError("mail should be Only Gmail..")
        
    #     if inputPwd != inputRPwd:
    #         raise forms.ValidationError("Password Should Match")