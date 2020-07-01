from django import forms

class MessageSend(forms.Form):
    name = forms.CharField()
    mail = forms.EmailField()
    Message = forms.CharField()
    date = forms.DateField()
    
    def clean_name(self):
        nme = self.cleaned_data['name']
        
        if len(nme) < 5:
            raise forms.ValidationError("Name should be Greater than 4")
        else:
            return nme