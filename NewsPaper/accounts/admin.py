from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment, Subscriber

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating')
    list_filter = ('author', 'postCategory')
    search_fields = ('title', 'author', 'postCategory')

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Subscriber)