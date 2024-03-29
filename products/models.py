from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    This model defines the categories for the
    Products
    """
    class Meta:
        verbose_name_plural = 'Categories'

    AMETHYST = "Amethyst"
    CALCITE = "Calcite"
    QUARTZ = "Quartz"
    CATEGORY_CHOICES = [
        (AMETHYST, "Amethyst"),
        (CALCITE, "Calcite"),
        (QUARTZ, "Quartz"),
    ]
    name = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=QUARTZ,
    )

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total / self.reviews.count()

        return 0


class Review(models.Model):
    """
    This model allows the creation and
    storage of a product rating and review
    """
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
