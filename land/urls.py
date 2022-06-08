from django.urls import include, re_path
from django.urls import path
from .views import edit_land, land_form, land_list, land_profile, edit_land, land,landexplanation
urlpatterns=[
    path("land", land, name="land"),
    path("register/", land_form, name="land_form"),
    path("list/", land_list, name="land_list"),
    path("profile/<int:id>/", land_profile, name="land_profile"),
    path("edit/<int:id>/", edit_land, name="edit_land"),
    path("landexplanation/", landexplanation, name="landexplanation"),


]