
from dataclasses import fields
from fileinput import FileInput
from django.forms import ModelForm
from django import forms
from .models import Blog

class BlogForm (ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image',
                  'photo_caption']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'description-input'}),
        }