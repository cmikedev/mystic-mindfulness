from django.contrib import admin
from .models import *


admin.site.register(Photo)
admin.site.register(Review)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'slug',
        'image',
        'price',
        )
    prepopulated_fields = {'slug': ('name',)}
