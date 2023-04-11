from django.db import models


class Quote(models.Model):
    body = models.CharField(max_length=750)
    author = models.CharField(max_length=750)
