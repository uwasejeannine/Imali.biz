from django.urls import include, re_path
from django.urls import path

from developer.views import developer, developer_form,develoxplan,edit_developer

urlpatterns=[
    path("developer", developer, name="developer"),
    path("register/", developer_form, name="developer_form"),
    path("develoxplan",develoxplan, name="develoxplan"),
    path("edit/<int:id>/", edit_developer, name="edit_developer"),


]