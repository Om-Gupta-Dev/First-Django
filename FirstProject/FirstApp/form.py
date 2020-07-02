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
    password = forms.CharField(widget = forms.PasswordInput)
    rpassword = forms.CharField(widget = forms.PasswordInput)
    date = forms.DateField()
        
    def clean(self):
        cleaned_data = super().clean()
        
        # inputName = cleaned_data['name']
        inputMail = cleaned_data['mail']
        inputPwd = cleaned_data['password']
        inputRPwd = cleaned_data['rpassword']
        
        # if inputName.isalpha() == False :
        #     raise forms.ValidationError("Name should Only Contain Alphabets")
        if inputMail[-10:] != "@gmail.com":
            raise forms.ValidationError("mail should be Only Gmail..")
        if inputPwd != inputRPwd:
            raise forms.ValidationError("Password Should Match")