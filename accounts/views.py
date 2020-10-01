from django.contrib.auth import login, logout,authenticate
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Jobseeker, Jobcreator,User,skills
from .forms import JobseekerForm,JobcreatorForm
from django.views.generic import CreateView 


def register(request):
    return render(request, "register.html")
    
class registerUser(CreateView):
    model = User
    form_class= JobseekerForm
    template_name= '../templates/registerUser.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("login")

    

class registerEmp(CreateView):
    model=User
    form_class= JobcreatorForm
    template_name= '../templates/registerEmp.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("login")

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_jobseeker:
                    login(request,user)
                    return redirect('userProfile')
                else:
                    login(request,user)
                    return redirect('empProfile')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")

    return render(request, '../templates/login.html',
    context={'form': AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

def skillsform(request):
    if request.method == "POST":
        id= request.POST["id"]
        category1 = request.POST["category1"]
        category2 = request.POST["category2"]
        category3 = request.POST["category3"]
        category4 = request.POST["category4"]
        category5 = request.POST["category5"]
        category6 = request.POST["category6"]
        query = request.POST["query"]
        title = request.POST["title"]
    
        user_skills = skills(id=id,category1=category1,category2=category2,category3=category3,category4=category4,category5=category5,category6=category6,query=query,title=title)
        user_skills.save()
        return redirect("login.html")

    else:
        return render(request, "skillsform.html")


 
def userProfile(request):
    return render(request, "userProfile.html")   

def empProfile(request):
    return render(request, "empProfile.html")  


