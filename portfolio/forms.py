from django import forms
from .models import portfolio

class PortfolioForms(forms.ModelForm):
    class Meta:
        model = portfolio
        fields = '__all__'