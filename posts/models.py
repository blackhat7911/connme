from django.db import models
from accounts.models import Profile

class Image(models.Model):
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    captions = models.TextField(null=True)
    images = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#class Like(models.Model):
