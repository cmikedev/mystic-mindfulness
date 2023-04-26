from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_details'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:pk>/', UpdatePostView.as_view(), name='edit_post'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
    path('comment/<int:pk>/', AddCommentView.as_view(), name='add_comment'),
]
