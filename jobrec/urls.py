from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
<<<<<<< HEAD
    #path("postjob", views.postjob, name="postjob"),
=======
>>>>>>> db34ad5806e1102e071e82ac2d2df294b61ac44c
    path("jobs", views.jobs, name="jobs"),
    path("jobpost", views.jobPost.as_view(), name="jobpost"),
    path("postjobSubmission", views.postjobSubmission, name="postjobSubmission"),
]
