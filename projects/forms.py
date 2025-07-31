from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'prerequisites', 'max_binomes']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'prerequisites': forms.Textarea(attrs={'rows': 3}),
        }