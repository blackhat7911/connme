from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post, Image

def index(request, pid):
    posts = Post.objects.get(id=pid)
    images = Image.objects.filter(name=posts)
    context = {
        'posts': posts,
        'images': images
        }
    return render(request, "frontend/home.html", context)
