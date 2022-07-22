from django.urls import include, re_path
from django.urls import path
from .views import  mach_form, mach_list
urlpatterns=[
    path("register/", mach_form, name="mach_form"),
    path("list/", mach_list, name="mach_list"),
   


]