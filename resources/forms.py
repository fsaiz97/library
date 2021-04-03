from django import forms
from .models import Resource


# DataFlair
class ResourceCreate(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'
