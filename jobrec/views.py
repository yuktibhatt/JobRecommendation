from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def postjob(request):
     return render(request, "postjob.html")
     

