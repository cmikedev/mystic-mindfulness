from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-details'),
    path('add/', views.add_post, name='add-post'),
    #path('edit/<int:pk>/', views.edit_post, name='edit-post'),
    path('edit/<int:pk>/', UpdatePostView.as_view(), name='edit-post'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete-post'),
]
