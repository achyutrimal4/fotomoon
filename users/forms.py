from django import forms
from . models import ContactMail
from django.forms import ModelForm



class ContactForm(ModelForm):
    class Meta:
        model=ContactMail
        fields = ['full_name', 'email', 'phone_number', 'subject', 'message']
        
