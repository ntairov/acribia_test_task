from django.db import models


class UrlField(models.Model):
    url_field = models.URLField()

    def __str__(self):
        return f'{self.url_field}'


class StatusCodeField(models.Model):
    status = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.status}'
