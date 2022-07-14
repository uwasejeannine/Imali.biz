from django.urls  import path
from .views import data_list,data_form
urlpatterns=[
    path("list/", data_list, name="data_list"),
    path("register/", data_form, name="data_form"),
]
