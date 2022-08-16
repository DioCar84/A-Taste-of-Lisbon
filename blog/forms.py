from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment


class PostForm(ModelForm):
    """
    The PostForm class defines the user form output for the Post model class.
    """
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        """
        The Meta class defines which model is associated and from that model,
        which fields will be accessible to the user.
        """
        model = Post
        fields = (
            'title',
            'featured_image',
            'excerpt',
            'meal_type',
            'dish_type',
            'content'
        )


class CommentForm(ModelForm):
    """
    The CommentForm class defines the user
    form output for the Comment model class.
    """
    class Meta:
        """
        The Meta class defines which model is associated and from that model,
        which fields will be accessible to the user.
        """
        model = Comment
        fields = ('body', )
