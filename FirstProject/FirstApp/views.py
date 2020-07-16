from django.shortcuts import render

import datetime

from FirstApp.models import Message
from FirstApp import form as firstForm

from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

date = datetime.datetime.now()
dt = {'name':'Om Gupta' , 'date':date }

# def index(request):
#     # date = datetime.datetime.now()
#     # count = int(request.session.get('sessioncount' , 0 ))
#     # count += 1
#     # request.session['sessioncount'] = count
#     # request.session.set_expiry(60)  #expiry time in seconds..
#     # exp = request.session.get_expiry_date()
#     indexPage = {'head1':'First Heading in index Page' , 
#                  'para1':'First Paragraph in index Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 'name':'Om Gupta' , 'date':date , 
                 
#                  'head2':'Second Heading in index Page' , 
#                  'para2':'Second Paragraph in index Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 
                 
#                  'head3':'Third Heading in index Page' , 
#                  'para3':'Third Paragraph in index Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!'}
#     response = render(request , 'FirstApp/index.html' , context = indexPage)
#     return response

class index(TemplateView):
    template_name = 'FirstApp/index.html'
    # def get(self , request):
    #     return HttpResponse('This is First Class Based View ') 
    # Passing Context Data
    def get_context_data(self , **kwargs):
        context = super().get_context_data()
        context['head1'] = 'First Class Based Template Page'
        return context

def home(request):
    date = datetime.datetime.now()
    count = int(request.COOKIES.get('count' , 0 ))
    count += 1  
    homePage = {'head1':'First Heading in home Page' , 
                'para1':'First Paragraph in home Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! ' , 
                
                'head2':'Second Heading in home Page' , 'name':'Om Gupta' , 'date':date , 
                'para2':'Second Paragraph in home Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 
                
                'head3':'Third Heading in home Page' , 
                'para3':'Third Paragraph in home Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 
                
                'count':count}
    response = render(request , 'FirstApp/home.html' , context = homePage)
    response.set_cookie('count' , count , max_age = 60)  #age limit for cookie
    return response

# Function Based Views FBV More Powerful

# def contact(request):
#     date = datetime.datetime.now()
#     data = Message.objects.all() 
    
#     if request.method == "GET":
#         forms = firstForm.MessageSend()
#         count = int(request.COOKIES.get('count' , 0 ))
#         count += 1
#         response = render(request , 'FirstApp/contact.html' , context = {'data':data , 'form':forms , 'count':count})
#         response.set_cookie('count' , count , max_age = 60)
#         return response

# Class Based Views FBV Less Powerful Than FBV's

class contact(View):
    # model = Message
    # Default template name : "message_List.html"
    # Default context name : "object_list"
    
    def get_context_data(self, **kwargs):
        data = Message.objects.all() 
        context = super().get_context_data(**kwargs)
        context["data"] = data
        print(context)
        return context
    
    def get(self, request, *args, **kwargs):
        data = Message.objects.all() 
        forms = firstForm.MessageSend()
        return render(request , 'FirstApp/message_List.html' , context = {'data':data , 'form':forms})
    
    def post(self , request , *args , **kwargs):
        data = Message.objects.all() 
        forms = firstForm.MessageSend(request.POST)
        if forms.is_valid():
            print("\n\tFORM VALIDATION SUCCESS.. PRINTING USER DATA..\n")
            print("Name : " , forms.cleaned_data['name'] )
            print("e-Mail : " , forms.cleaned_data['mail'] )
            print("Message : " , forms.cleaned_data['Message'] )
            print("Date : " , forms.cleaned_data['date'] )
            # saving data as session
            request.session['name'] = forms.cleaned_data['name']
            request.session['mail'] = forms.cleaned_data['mail']
            request.session['Message'] = forms.cleaned_data['Message']
            request.session['date'] = str(forms.cleaned_data['date']) 
            # retrieving Session data to show in thank.html
            sName = request.session['name']
            sMail = request.session['mail']
            sMessage = request.session['Message']
            sDate = request.session['date']
            
            forms.save(commit=True)
            return render(request , 'FirstApp/thank.html' , context = {'name':sName,'mail':sMail,'message':sMessage,'date':sDate})
        else:
            return render(request , 'FirstApp/contact.html' , context = {'data':data , 'form':forms})
        
    # if request.method == "POST":
    #     forms = firstForm.MessageSend(request.POST)
    #     if forms.is_valid():
    #         print("\n\tFORM VALIDATION SUCCESS.. PRINTING USER DATA..\n")
    #         print("Name : " , forms.cleaned_data['name'] )
    #         print("e-Mail : " , forms.cleaned_data['mail'] )
    #         print("Message : " , forms.cleaned_data['Message'] )
    #         print("Date : " , forms.cleaned_data['date'] )
    #         # saving data as session
    #             # request.session['name'] = forms.cleaned_data['name']
    #             # request.session['mail'] = forms.cleaned_data['mail']
    #             # request.session['Message'] = forms.cleaned_data['Message']
    #             # request.session['date'] = str(forms.cleaned_data['date']) 
    #         # retrieving Session data to show in thank.html
    #             # sName = request.session['name']
    #             # sMail = request.session['mail']
    #             # sMessage = request.session['Message']
    #             # sDate = request.session['date']
            
    #         forms.save(commit=True)
    #         return render(request , 'FirstApp/thank.html')
    #     else:
    #         return render(request , 'FirstApp/contact.html' , context = {'data':data , 'form':forms})
        
        
def signup(request):
    if request.method == "GET":
        form = firstForm.signup()
        return render(request , 'registration/signup.html' , {'form':form})
    
    if request.method == "POST":
        form = firstForm.signup(request.POST)
        # if form.is_valid():          #applicable for only default password hashers 
        #     form.save()
        
        if form.is_valid():
            # form.save()
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
        else:
            return render(request , 'registration/signup.html' , {'form':form})