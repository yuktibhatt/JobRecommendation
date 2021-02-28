from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path
from . import views

urlpatterns = [
    path("register/",views.register, name="register"),
    #re_path("accounts/update/(?P<slug>[\-\w]+)/$", views.userUpdate.as_view(), name="views.userUpdate"),
    path("userUpdate",views.userUpdate.as_view(), name="userUpdate"),
    path("registerUser",views.registerUser.as_view(), name="registerUser"),
    path("registerEmp",views.registerEmp.as_view(), name="registerEmp"),
    path("login",views.login_view, name="login"),
    path("logout",views.logout_view, name="logout"),
    path("userProfile",views.userProfile, name="userProfile"),
    path("empProfile",views.empProfile, name="empProfile"),
    #path("userProfile/<int:pk>",views.updateProfile,name="updateProfile"),

    
   ]
