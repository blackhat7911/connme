from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post, Image
from accounts.models import Profile

def index(request, pid):
    user = request.user
    posts = Post.objects.get(id=pid)
    images = Image.objects.filter(name=posts)
    profile = Profile.objects.get(user=user)
    context = {
        'posts': posts,
        'images': images,
        'profile': profile
        }
    return render(request, "frontend/home.html", context)
