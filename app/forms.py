from .models import StudentModels
from django import forms

class StudentModelForms(forms.ModelForm):
    class Meta:
        model=StudentModels
        fields=['name','age']