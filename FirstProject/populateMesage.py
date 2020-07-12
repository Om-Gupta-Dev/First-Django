import os
from faker import Faker
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'FirstProject.settings')
import django
django.setup()

from FirstApp.models import *

from CRUD.models import *

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
    
    
# populate(11)

# For CRUD APP 

def populateEmployee(n):
    for i in range(n):
        feNo = int(fake.numerify())
        feName = fake.name()
        feSalary = random.randint(100000,200000)
        feAdddress = fake.address()
        Employee.objects.get_or_create(eNo = feNo , 
                                eName = feName , 
                                eSalary = feSalary , 
                                eAdddress = feAdddress)
    
populateEmployee(10)