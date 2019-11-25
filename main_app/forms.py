from django import forms
from .models import UrlField


class UrlFieldForm(forms.ModelForm):
    class Meta:
        model = UrlField
        fields = ['url_field', ]

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url_field')
        # If url is not empty and doesn't endswith '/'
        if not url.endswith('/'):
            url += '/'
            cleaned_data['url_field'] = url
        return cleaned_data
