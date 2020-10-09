from django.db import models

# Create your models here.
class JoblistTable(models.Model):
    jobid = models.CharField(primary_key=True, max_length=20)
    advertiserurl = models.CharField(max_length=500, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    jobstatus = models.CharField(max_length=100, blank=True, null=True)
    jobdescription = models.TextField(blank=True, null=True)
    joblocation = models.CharField(max_length=200, blank=True, null=True)
    jobtitle = models.CharField(max_length=200, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    
