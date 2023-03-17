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


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        related_name='products',
        null=TRUE,
        blank=TRUE,
        on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    image = CloudinaryField('image')
    description = models.TextField(max_length=1000)
    price = models.FloatField()

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name

