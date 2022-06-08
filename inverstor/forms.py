from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Investor

class InvestorForm(forms.ModelForm):
    class Meta:
        model= Investor
        fields= "__all__"