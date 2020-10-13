from django import forms
from .models import *

class JobPostForm(forms.ModelForm):
    jobid = forms.CharField()
    advertiserurl = forms.CharField()
    company = forms.CharField()
    jobstatus = forms.CharField()
    jobdescription = forms.CharField()
    joblocation = forms.CharField()
    jobtitle = forms.CharField()
    skills = forms.CharField()
    jobtitle = forms.CharField()

    class Meta:
        model = JoblistTable
        fields = ('jobid','advertiserurl','company','jobstatus','jobdescription','joblocation','jobtitle','skills')

