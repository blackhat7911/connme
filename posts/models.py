from django.db import models
from accounts.models import Profile

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    captions = models.TextField(null=True)

    def __str__(self):
        return str(self.author.user.username)
    
class Image(models.Model):
    name = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.FileField(blank=True, null=True, upload_to='media')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#class Like(models.Model):
