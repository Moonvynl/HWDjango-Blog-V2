from django.contrib import admin
from .models import Comment, Author, Post


admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Post)


