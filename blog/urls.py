from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-details'),
    path('add/', views.add_post, name='add-post'),
]
