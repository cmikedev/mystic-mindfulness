from django.db import models
#from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Photo(models.Model):
    """
    This model allows for the uploading of
    photos to Cloudinary
    """
    title = models.CharField(max_length=100)
    image = models.ImageField('image')

    def __str__(self):
        return self.title


"""class Category(models.Model):
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
"""

class Product(models.Model):
    #category = models.ForeignKey(
    #    'Category',
    #    null=True,
    #    blank=True,
    #    on_delete=models.SET_NULL)
    AMETHYST = "Amethyst"
    CALCITE = "Calcite"
    QUARTZ = "Quartz"
    CATEGORY_CHOICES = [
        (AMETHYST, "Amethyst"),
        (CALCITE, "Calcite"),
        (QUARTZ, "Quartz"),
    ]
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=QUARTZ,
    )
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name
    
    #def get_absolute_url(self):
    #    return reverse('detail', kwargs={'slug': self.slug, 'pk': self.pk})
    
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
