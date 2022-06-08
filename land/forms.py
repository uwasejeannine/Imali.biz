from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Land

class LandForm(forms.ModelForm):
    class Meta:
        model= Land
        fields= "__all__"