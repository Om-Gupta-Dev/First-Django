from django import forms
from django.core import validators

class MessageSend(forms.Form):
    name = forms.CharField()
    mail = forms.EmailField()
    Message = forms.CharField(widget=forms.Textarea)
    date = forms.DateField()
    
    def clean_name(self):
        nme = self.cleaned_data['name']
        
        if len(nme) < 5:
            raise forms.ValidationError("Name should be Greater than 4")
        else:
            return nme
        
    def clean_Message(self):
        inputMessage = self.cleaned_data['Message']
        
        if len(inputMessage) < 10 or 200 < len(inputMessage):
            raise forms.ValidationError("Message length Should be greater than 10 and less than 200..")
        else:
            return inputMessage