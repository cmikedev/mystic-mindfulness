from django.db import models
from cloudinary.models import CloudinaryField


class Photo(models.Model):
    """
    This model allows for the uploading of
    photos to Cloudinary
    """
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name