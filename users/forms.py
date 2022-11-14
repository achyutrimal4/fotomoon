from django import forms
from . models import ContactMail, Booking
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'


class ContactForm(ModelForm):
    class Meta:
        model=ContactMail
        fields = ['full_name', 'email', 'phone_number', 'subject', 'message']
        
class BookingForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea
                              (attrs=
                               {'placeholder': 
                                   'If you want to request for multiple services, mention here. Explain about your event here. '
                                   }
                               ))
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone_number','date', 'service_type', 'message']
        widgets = {
            'date': DateInput(),
        }