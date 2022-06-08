from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Buyer

class BuyerForm(forms.ModelForm):
    class Meta:
        model= Buyer
        fields= "__all__"