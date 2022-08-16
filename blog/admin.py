from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    The PostAdmin class will add the Post model to admin page.
    Also defines the content field as a
    Summernote field to use the text editor,
    as well as prepopulating the slug based on the post title.
    """
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    The CommentAdmin class will add the Comment model to admin page.
    Also allows the admin to approve comments and,
    to filter the comments objects by their approved status.
    """
    list_filter = ('approved',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
