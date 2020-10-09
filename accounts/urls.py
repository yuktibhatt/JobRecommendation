from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("register/",views.register, name="register"),
    path("registerUser",views.registerUser.as_view(), name="registerUser"),
    path("registerEmp",views.registerEmp.as_view(), name="registerEmp"),
    path("login",views.login_view, name="login"),
    path("logout",views.logout_view, name="logout"),
    path("userProfile",views.userProfile, name="userProfile"),
    path("empProfile",views.empProfile, name="empProfile"),
    
    
   ]