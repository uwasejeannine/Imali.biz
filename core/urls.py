from django.urls  import path
from .views import home,data
urlpatterns=[
    path("", home, name="home"),
    path("data", data, name="data"),



]