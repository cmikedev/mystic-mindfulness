from django.contrib import admin
from .models import *


admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'date_posted',
        'title',
        'author',
        'image',
        )
