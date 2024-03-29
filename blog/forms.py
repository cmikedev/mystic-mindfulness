from django import forms
from .widgets import CustomClearableFileInput
from .models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
