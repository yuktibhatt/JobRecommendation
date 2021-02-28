from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("home",views.home,name='home'),
    path("jobs", views.jobs, name="jobs"),
    path("jobpost", views.jobPost.as_view(), name="jobpost"),
    # path("postjobSubmission", views.postjobSubmission, name="postjobSubmission"),
]
