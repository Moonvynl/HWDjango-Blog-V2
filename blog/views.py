from django.shortcuts import render
from blog.models import Post

def get_posts(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(
        request,
        template_name="blog/post_list.html",
        context=context
    )
