from django import forms

class MessageSend(forms.Form):
    name = forms.CharField()
    mail = forms.EmailField()
    Message = forms.CharField()
    date = forms.DateField()