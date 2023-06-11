from django import forms
from .models import About

class AboutForms(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'