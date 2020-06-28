from django.shortcuts import render
import datetime
from FirstApp.models import Message

# Create your views here.

date = datetime.datetime.now()
dt = {'name':'Om Gupta' , 'date':date }

def index(request):
    date = datetime.datetime.now()
    indexPage = {'head1':'First Heading in index Page' , 
                 'para1':'First Paragraph in index Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 'name':'Om Gupta' , 'date':date , 
                 
                 'head2':'Second Heading in index Page' , 
                 'para2':'Second Paragraph in index Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 
                 
                 'head3':'Third Heading in index Page' , 
                 'para3':'Third Paragraph in index Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!'}
    return render(request , 'FirstApp/index.html' , context = indexPage)

def home(request):
    date = datetime.datetime.now()
    homePage = {'head1':'First Heading in home Page' , 
                'para1':'First Paragraph in home Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! ' , 
                
                'head2':'Second Heading in home Page' , 'name':'Om Gupta' , 'date':date , 
                'para2':'Second Paragraph in home Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 
                
                'head3':'Third Heading in home Page' , 
                'para3':'Third Paragraph in home Page.. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!'}
    return render(request , 'FirstApp/home.html' , context = homePage)


def contact(request):
    date = datetime.datetime.now()
    
    data = Message.objects.all()
    print(data)
    print(type(data))
    
    return render(request , 'FirstApp/contact.html' , context = {'data':data})
    
