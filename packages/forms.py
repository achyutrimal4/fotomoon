from django.forms import ModelForm
from django import forms
from .models import Packages


class PackageForm(ModelForm):
    class Meta:
        model=Packages
        fields = ['title', 'available', 'price', 'photo']
        