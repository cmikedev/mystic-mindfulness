from django.contrib import admin
from .models import *


admin.site.register(Photo)
admin.site.register(Review)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        )
    prepopulated_fields = {'friendly_name': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'friendly_name',
        'image',
        'price',
        )
    prepopulated_fields = {'friendly_name': ('name',)}
