from django.forms import ModelForm
from django import forms
from .models import Photo, Portfolio, PhotoPortfolio


class PhotoForm(ModelForm):
    class Meta:
        model=Photo
        fields = ['description', 'photo']
        
class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name', 'photo']
        
class PhotoPortfolioForm(ModelForm):
    class Meta:
        model = PhotoPortfolio
        fields = ['photo','portfolio','description']
        