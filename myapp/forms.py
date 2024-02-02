from .models import *
from django import forms

class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ['name','email']
