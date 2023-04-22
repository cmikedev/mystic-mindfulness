from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
        )
    body = RichTextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_posted"]

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('blog')

    def get_image(self):
        try:
            url = self.image.url
        except:
            url='/media/noimage.png'
        return url


class Comment(models.Model):
    post = models.ForeignKey(
            Post, related_name="comments", on_delete=models.CASCADE
        )
    name = models.CharField(max_length=255)
    #body = models.TextField(max_length=500)
    body = RichTextField(null=True, blank=True, max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_added"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
