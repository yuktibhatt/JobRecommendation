from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_jobseeker = models.BooleanField(default=False)
    is_jobcreator = models.BooleanField(default=False)
     

class Jobseeker(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key= True)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img')
    address = models.CharField(max_length=100)
    # category1 = models.CharField(max_length=100)
    # category2 = models.CharField(max_length=100)
    # category3 = models.CharField(max_length=100)
    # category4 = models.CharField(max_length=100)
    # category5 = models.CharField(max_length=100)
    # category6 = models.CharField(max_length=100)
    # query  = models.CharField(max_length=100)
    # title  = models.CharField(max_length=100)
    

class Jobcreator(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key= True)
    orgname = models.CharField(max_length=50)
    contact = models.CharField(max_length=100)
    

# class skills(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key= True, db_column="id")
#     category1 = models.CharField(max_length=100)
#     category2 = models.CharField(max_length=100)
#     category3 = models.CharField(max_length=100)
#     category4 = models.CharField(max_length=100)
#     category5 = models.CharField(max_length=100)
#     category6 = models.CharField(max_length=100)
#     query  = models.CharField(max_length=100)
#     title  = models.CharField(max_length=100)

