from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *
from django_select2.forms import Select2MultipleWidget

skills_choices = [
    ('.net', '.Net'),
    ('.net-core','.Net-core'),
    ('ajax','Ajax'), 
    ('amazon-web-services','Amazon-web-services'), 
    ('angularjs','Angularjs'), 
    ('architecture','Architecture'), 
    ('asp.net','asp.net'), 
    ('azure','Azure'), 
    ('big-data','Big-data'),
    ('c#', 'C#'),
    ('c','C'),
    ('c++','C++'), 
    ('cloud','Cloud'), 
    ('css','Css'), 
    ('docker','Docker'), 
    ('hadoop','Hadoop'), 
    ('html','Html'), 
    ('java','Java'), 
    ('javascript','Javascript'), 
    ('jquery','Jquery'), 
    ('keras','Keras'), 
    ('machine-learning','Machine-learning'), 
    ('mongodb','Mongodg'), 
    ('mysql','mysql'), 
    ('oracle','Oracle'), 
    ('php','PHP'), 
    ('postgresql','Postgresql'), 
    ('project-management','Project-management'), 
    ('python','Python'), 
    ('r','R'), 
    ('reactjs','Reactjs'), 
    ('rest','Rest'), 
    ('ruby','Ruby'), 
    ('scala','Sacla'), 
    ('scikit-learn','Scikit-learn'), 
    ('software-design','Software-design'), 
    ('spark','Spark'), 
    ('sql','Sql'), 
    ('xml','Xml')
    
    
]


class JobseekerForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    image = forms.ImageField(required=True)
    address = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    skills = forms.MultipleChoiceField(
        #required=False,
        #widget=forms.CheckboxSelectMultiple,
        widget=Select2MultipleWidget,
        choices=skills_choices,
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields= ('first_name','last_name', 'username','email', 'image','address','phone')
      


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_jobseeker = True
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        user.email=self.cleaned_data.get('email')
        user.save()
        jobseeker= Jobseeker.objects.create(user=user)
        jobseeker.phone=self.cleaned_data.get('phone')
        jobseeker.address=self.cleaned_data.get('address')
        jobseeker.image=self.cleaned_data.get('image')
        jobseeker.skills = self.cleaned_data.get('skills')
        jobseeker.save()
        return user

class JobcreatorForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    orgname = forms.CharField(label='Organization Name',required=True)
    email = forms.CharField(label='Organization Email',required=True)
    contact= forms.CharField(label='Organization Contact',required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields= ('first_name','last_name', 'username','orgname', 'email','contact')
        
    

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_jobcreator = True
        user.is_staff= True
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        user.email=self.cleaned_data.get('email')
        user.save()
        jobcreator= Jobcreator.objects.create(user=user)
        jobcreator.orgname=self.cleaned_data.get('orgname')
        jobcreator.contact=self.cleaned_data.get('contact')
        jobcreator.save()
        return user