from django.urls import path

import blog.views as blog_views

urlpatterns = [
    path("", blog_views.posts_list, name="posts_list"),
    path("<int:post_id>", blog_views.view_post, name="post_details"),
    path("author/<int:author_id>", blog_views.author_posts, name="author_posts")
]
