from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, \
    DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


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
            return redirect(reverse('post_details', args=[post.id]))
        else:
            messages.error(
                request,
                'Failed to add post. Please ensure the form is valid.'
                )
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


class UpdatePostView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_message = 'Successfully updated post!'
    template_name = 'blog/edit_post.html'


class DeletePostView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog')


class AddCommentView(LoginRequiredMixin, SuccessMessageMixin,
                     generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    success_url = reverse_lazy('blog')
    success_message = 'Thank you. Your comment has been posted.'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user.username
        return super().form_valid(form)
