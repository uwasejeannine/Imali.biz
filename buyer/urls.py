from django.urls import include, re_path
from django.urls import path
from .views import buyer_form, buyer_list,buyer_profile, edit_buyer, buyer,buyerexplan
urlpatterns=[
    path("buyer", buyer, name="buyer"),
    path("register/", buyer_form, name="buyer_form"),
    path("list/", buyer_list, name="buyer_list"),
    path("profile/<int:id>/", buyer_profile, name="buyer_profile"),
    path("edit/<int:id>/", edit_buyer, name="edit_buyer"),
    path("buyerexplan", buyerexplan, name="buyerexplan"),

]