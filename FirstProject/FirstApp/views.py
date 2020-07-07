from django.shortcuts import render
import datetime
from FirstApp.models import Message
from FirstApp import form

# Create your views here.

date = datetime.datetime.now()
dt = {'name':'Om Gupta' , 'date':date }

def index(request):
    date = datetime.datetime.now()
    count = int(request.session.get('sessioncount' , 0 ))
    count += 1
    indexPage = {'head1':'First Heading in index Page' , 
                 'para1':'First Paragraph in index Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 'name':'Om Gupta' , 'date':date , 
                 
                 'head2':'Second Heading in index Page' , 
                 'para2':'Second Paragraph in index Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 
                 
                 'head3':'Third Heading in index Page' , 
                 'para3':'Third Paragraph in index Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 
                 
                 'count':count}
    response = render(request , 'FirstApp/index.html' , context = indexPage)
    request.session['sessioncount'] = count
    return response

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


def contact(request):
    date = datetime.datetime.now()
    data = Message.objects.all() 
    
    if request.method == "GET":
        forms = form.MessageSend()
        count = int(request.COOKIES.get('count' , 0 ))
        count += 1
        response = render(request , 'FirstApp/contact.html' , context = {'data':data , 'form':forms , 'count':count})
        response.set_cookie('count' , count , max_age = 60)
        return response
        
    if request.method == "POST":
        forms = form.MessageSend(request.POST)
        if forms.is_valid():
            print("\n\tFORM VALIDATION SUCCESS.. PRINTING USER DATA..\n")
            print("Name : " , forms.cleaned_data['name'] )
            print("e-Mail : " , forms.cleaned_data['mail'] )
            print("Message : " , forms.cleaned_data['Message'] )
            print("Date : " , forms.cleaned_data['date'] )
            
            forms.save(commit=True)
            return render(request , 'FirstApp/thank.html')
        else:
            return render(request , 'FirstApp/contact.html' , context = {'data':data , 'form':forms})
        
        