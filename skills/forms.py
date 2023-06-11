from django import forms
from .models import Skills

class SkillForm(forms.ModelForm):
    class Meta :
        model = Skills
        fields = '__all__'