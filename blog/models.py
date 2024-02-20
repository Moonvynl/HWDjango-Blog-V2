from django.db import models
from django.utils import timezone
from datetime import timedelta


class Author(models.Model):
    name = models.CharField(max_length=63)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length = 63)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now = True)
    photo = models.ImageField(default=None)
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING, default = None, related_name="posts")

    def __str__(self):
        return self.title
    
    def published_recently(self):
        return timezone.now() - timedelta(days=7) < self.published_date


class Comment(models.Model):
    author_name = models.CharField(max_length=63)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete = models.DO_NOTHING, default = None, related_name="comments")
    created_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.text
    