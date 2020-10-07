from django import forms
from .models import *

class JobPostForm(forms.ModelForm):
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
        fields = ('advertiserurl','company','jobstatus','jobdescription','joblocation','jobtitle','skills','jobid')


