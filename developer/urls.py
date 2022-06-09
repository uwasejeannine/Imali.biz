from django.urls import include, re_path
from django.urls import path

from developer.views import developer, developer_form,develoxplan

urlpatterns=[
    path("developer", developer, name="developer"),
    path("register/", developer_form, name="developer_form"),
    path("develoxplan",develoxplan, name="develoxplan"),

]