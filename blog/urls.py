from django.urls import path

import blog.views as blog_views

urlpatterns = [
    path('', blog_views.get_posts, name='post_list'),
]