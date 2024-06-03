from django.shortcuts import render, get_object_or_404
from .models import Post


""" The following views will show the pages
for the list of blog posts and then the detail
for each blog post. """

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/blog_detail.html', {'post': post})


