from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import DataList

class DataForm(forms.ModelForm):
    class Meta:
        model= DataList
        fields= "__all__"