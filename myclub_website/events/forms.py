from django import forms
from django.forms import ModelForm, widgets
from .models import Event, Venue

# Create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address',)
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }
# Add bootstrap classes
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
            'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Website'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),
        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'description', 'attendees',)
        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'Venue',
            'manager': 'Manager',
            'attendees': 'Attendees',
            'description': '',
        }
# Add bootstrap classes
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Event'}),
            'manager': forms.Select(attrs={'class':'form-select', 'placeholder':'Manager'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
        }