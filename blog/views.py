from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import PostForm
from django.contrib import messages


class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'


@login_required
def add_post(request):
    """ Add a post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('post-details', args=[post.id]))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()
        
    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
