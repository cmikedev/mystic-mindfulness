from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class SubscribedUsers(models.Model):
    """
    Store info for email newsletter
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    class Meta:
        verbose_name_plural = 'SubscribedUsers'

    def __str__(self):
        return self.email
