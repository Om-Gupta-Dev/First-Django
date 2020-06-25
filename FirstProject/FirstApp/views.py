from django.shortcuts import render
import datetime

# Create your views here.

date = datetime.datetime.now()
dt = {'name':'Om Gupta' , 'date':date }

def index(request):
    indexPage = {'head1':'First Heading in index Page' , 
                 'para1':'First Paragraph in index Page Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 'name':'Om Gupta' , 'date':date , 
                 
                 'head2':'Second Heading in index Page' , 
                 'para2':'Second Paragraph in index Page Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 
                 
                 'head3':'Third Heading in index Page' , 
                 'para3':'Third Paragraph in index Page Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!'}
    return render(request , 'FirstApp/index.html' , context = indexPage)

def home(request):
    homePage = {'head1':'First Heading in home Page' , 
                'para1':'First Paragraph in home Page Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! ' , 
                
                'head2':'Second Heading in home Page' , 'name':'Om Gupta' , 'date':date , 
                'para2':'Second Paragraph in home Page Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 
                
                'head3':'Third Heading in home Page' , 
                'para3':'Third Paragraph in home Page Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!'}
    return render(request , 'FirstApp/home.html' , context = homePage)


def contact(request):
    contactPage = {'head1':'First Heading in contact Page' , 
                   'para1':'First Paragraph in contact Page Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 'name':'Om Gupta' , 'date':date , 
                   
                   'head2':'Second Heading in contact Page' , 
                   'para2':'Second Paragraph in contact Page Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!' , 
                   
                   'head3':'Third Heading in contact Page' , 
                   'para3':'First Paragraph in contact Page Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae consectetur ab eligendi nemo voluptates inventore provident minus sunt in numquam!'}
    
    return render(request , 'FirstApp/contact.html' , context = contactPage)
    
