from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from .models import MailAddress

class CreateEmail(forms.ModelForm):
    class Meta:
        model = MailAddress
        fields = ('name', 'email',)
        labels = {
            'name': '',
            'email': '',
        }

        widgets = {
                    'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
                    'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),
        }

class SendToEmails(forms.ModelForm):
    class Meta:
        model = MailAddress
        fields = ('name', 'email',)
        labels = {
            'name': '',
            'email': '',
        }

        widgets = {
                    'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
                    'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),
        }