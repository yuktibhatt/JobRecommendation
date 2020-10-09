from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_jobseeker = models.BooleanField(default=False)
    is_jobcreator = models.BooleanField(default=False)
     

class Jobseeker(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key= True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank= True, null = True)
    #skills = models.ManyToManyField(Skills)
    skill_choices = [
    ('.net', '.Net'),
    ('c#', 'C#'),
    ('python', 'Python'),
    ('sql','Sql'),
    ('html','Html'),
    ('css','Css'),
    ]
    #skills = models.CharField(max_length=100,blank=True,verbose_name="Select")
    skills = models.TextField()

class Jobcreator(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key= True)
    orgname = models.CharField(max_length=50)
    contact = models.CharField(max_length=100)
    

class jobrec(models.Model):
    index = models.IntegerField(primary_key=False)
    jobid = models.CharField(max_length=50,default='Dice:')
    jobtitle = models.TextField(50)
    score = models.IntegerField(primary_key=False)

