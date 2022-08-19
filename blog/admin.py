from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Class for content field (text field in database) to be a Summernote field
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')

# Model to register posts moved to decorator @admin.register(Post)
# admin.site.register(Post)

# add the comment admin model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body') 
# an action that allows us to approve the comment
    actions = ['approve_comments']

# a method to approve comments
def approve_comments(self, request, queryset):
    queryset.update(approved=True)
