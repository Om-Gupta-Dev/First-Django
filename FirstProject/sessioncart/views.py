from django.shortcuts import render
from sessioncart import form

# Create your views here.

def index(request):
    if request.method == "POST":
        forms = form.cartForm(request.POST)
        if forms.is_valid():
            item =  forms.cleaned_data['item']
            quantity = forms.cleaned_data['quantity']
            request.session[item] = quantity
    return render(request , 'sessioncart/index.html' , {'form': form.cartForm})

def cart(request):
    return render(request , 'sessioncart/cart.html')

