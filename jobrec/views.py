from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import *
from .forms import *

def index(request):
    return render(request, "index.html")

import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:1234@localhost:5432/jobrec')
def jobs(request):
    df = pd.read_sql_table('accounts_jobseeker',engine)
    print(df)
    return render(request,"jobs.html")

def postjob(request):
     return render(request, "postjob.html")


class jobPost(TemplateView):
    model = JoblistTable
    
    template_name = '../templates/jobpost.html'
    def get(self,request):
        form = JobPostForm()
        return render(request,self.template_name,{'form':form})
   
   
    def post(self, request):
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            jobid = form.cleaned_data['jobid']
            advertiserurl = form.cleaned_data['advertiserurl']
            company = form.cleaned_data['company']
            jobstatus = form.cleaned_data['jobstatus']
            jobdescription = form.cleaned_data['jobdescription']
            joblocation = form.cleaned_data['joblocation']
            jobtitle = form.cleaned_data['jobtitle']
            skills = form.cleaned_data['skills']
            jobid = form.cleaned_data['jobid']
            form = JobPostForm()
            return redirect("index")

        args = {'form':form,'advertiserurl':advertiserurl,'company':company,'jobstatus':jobstatus,'jobdescription':jobdescription,'joblocation':joblocation,'jobtitle':jobtitle,'skills':skills,'jobid':jobid}
        return render (request,self.template_name,args)

def postjobSubmission(request):

    if request.method == 'POST':
        advertiserurl = request.POST.get('advertiserurl')
        company = request.POST.get('company')
        jobstatus = request.POST.get('jobstatus')
        jobdescription = request.POST.get('jobdescription')
        joblocation = request.POST.get('joblocation')
        jobtitle = request.POST.get('jobtitle')
        skills = request.POST.get('skills')
        jobid = request.POST.get('jobid')

        job_list = JoblistTable(advertiserurl=advertiserurl,company=company,jobstatus=jobstatus,jobdescription=jobdescription,joblocation=joblocation,jobtitle=jobtitle,skills=skills,jobid=jobid)
        job_list.save()
    else:
        return render(request,"postjob.html")
    
    return render(request,"index.html")


