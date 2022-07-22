from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import  Mach

class MachForm(forms.ModelForm):
    class Meta:
        model= Mach
        fields= "__all__"