from django.db import models
from django import forms

# Create your models here.
class MyForm(forms.Form):
    file = forms.FileField()