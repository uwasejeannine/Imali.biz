from django.urls import include, re_path
from django.urls import path
from .views import investor_form, investor_list, investor_profile, edit_investor, inverstor,investorexplanation
urlpatterns=[
    path("inverstor", inverstor, name="investor"),
    path("register/", investor_form, name="investor_form"),
    path("list/", investor_list, name="investor_list"),
    path("profile/<int:id>/", investor_profile, name="investor_profile"),
    path("edit/<int:id>/", edit_investor, name="edit_investor"),
    path("invdetails", investorexplanation, name="investorexplanation"),

]