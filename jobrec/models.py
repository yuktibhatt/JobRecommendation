from django.db import models
from accounts.models import Jobcreator,User

# Create your models here.
class JoblistTable(models.Model):
    advertiserurl = models.CharField(max_length=500, blank=True, null=True)
    company = models.CharField(max_length=2000, blank=True, null=True)
    jobstatus = models.CharField(max_length=500, blank=True, null=True)
    jobdescription = models.TextField(blank=True, null=True)
    joblocation = models.CharField(max_length=200, blank=True, null=True)
    jobtitle = models.CharField(max_length=200, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    salary = models.IntegerField(default=60000,null=True)
    createruser = models.ForeignKey(User,
        on_delete=models.CASCADE,
        null = True,
        default = None)