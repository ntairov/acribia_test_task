from django import forms
from .models import UrlField


class UrlFieldForm(forms.ModelForm):
    class Meta:
        model = UrlField
        fields = ['url_field', ]

