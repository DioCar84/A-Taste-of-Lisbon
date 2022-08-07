from django import forms
from django.forms import ModelForm
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget

class PostForm(ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'excerpt', 'meal_type', 'dish_type', 'content')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )