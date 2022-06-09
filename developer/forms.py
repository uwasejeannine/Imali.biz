from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Developer

class DeveloperForm(forms.ModelForm):
    class Meta:
        model=Developer
        fields= "__all__"