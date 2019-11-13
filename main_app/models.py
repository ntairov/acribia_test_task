from django.db import models


class UrlField(models.Model):
    url_field = models.URLField()

    def __str__(self):
        return f'{self.url_field}'
