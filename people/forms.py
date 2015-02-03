from __future__ import absolute_import
from django import forms

from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name',)
