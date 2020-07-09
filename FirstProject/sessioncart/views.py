from django.shortcuts import render
from sessioncart import form
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method == "POST":
        forms = form.cartForm(request.POST)
        if forms.is_valid():
            item =  forms.cleaned_data['item']              #or request.POST['item']
            quantity = forms.cleaned_data['quantity']       #or request.POST['quantity']
            request.session[item] = quantity
            request.session.set_expiry(0)
    return render(request , 'sessioncart/index.html' , {'form': form.cartForm})

@login_required
def cart(request):
    return render(request , 'sessioncart/cart.html')

