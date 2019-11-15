from django.contrib import admin
from .models import UrlField, StatusCodeField

admin.site.register(UrlField)
admin.site.register(StatusCodeField)