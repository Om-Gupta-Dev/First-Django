import os
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'FirstProject.settings')
import django
django.setup()

from FirstApp.models import *

fake = Faker()

def populate(n):
    for i in range(n):
        fname = fake.name()
        fmail = fake.email()
        fMessage = fake.catch_phrase()
        fdate = fake.date()
        Message.objects.get_or_create(name = fname , 
                                mail = fmail , 
                                Message = fMessage , 
                                date = fdate)
    
    
populate(11)