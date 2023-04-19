from django.contrib import admin
from .models import SubscribedUsers


@admin.register(SubscribedUsers)
class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'created_date',
        )
