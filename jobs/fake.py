import os 
import django
from random import randint
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobs.settings')
django.setup()
fake = Faker()
from jobApp import models
 

def PhoneNumber():
    digit = randint(7, 9)
    num = '' + str(digit)

    for i in range(9):
        num += str(randint(0, 9))
    return num

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager', 'Team leaer', 'Software Engineer'))
        feligibility = fake.random_element(elements=('B.Tech', 'M.Tech', 'MCA', 'Phd'))
        femail = fake.email()
        faddress = fake.address()
        fphonenumber = PhoneNumber()

        jobs_record = models.Hydjobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress, email = femail, phone_number=fphonenumber)

populate(20)