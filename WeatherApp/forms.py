from dataclasses import field, fields
from pyexpat import model
from tkinter import Widget
from django import forms
from . import models

class CityForm(forms.ModelForm):
    
    class Meta:
        model = models.City
        fields = ['name']
        widget = {'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter City'})}