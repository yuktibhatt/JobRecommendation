from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Jobseeker, Jobcreator,User

class JobseekerForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    image = forms.ImageField(required=True)
    address = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    
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