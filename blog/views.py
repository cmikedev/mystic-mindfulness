from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
