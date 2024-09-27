from django import forms
from .models import Project


class ProjectForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=1000, required=True)

    class Meta:
        model = Project
