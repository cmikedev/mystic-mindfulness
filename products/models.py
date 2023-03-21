from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


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
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        related_name='products',
        null=True,
        blank=True,
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
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug, 'pk': self.pk})
    
    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total >0 :
            return reviews_total / self.reviews.count()
        
        return 0


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.CASCADE
        )
    rating = models.IntegerField(default=3)
    comment = models.TextField()
    created_by = models.ForeignKey(
        User,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
