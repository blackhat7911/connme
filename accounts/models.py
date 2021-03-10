from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.username)

class Relationship(models.Model):
    RELATION = (
        ('following', 'following'),
        ('notfollowing', 'notfollowing'),
    )
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    following = models.ManyToManyField(Profile, related_name="following")