from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(blank=True, null=True)
    full_name = models.CharField(null=True, max_length=255)
    about = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

class Relationship(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(Profile, related_name='following')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

    @classmethod
    def follow(cls, user, another_acc):
        obj, create = cls.objects.get_or_create(user=user)
        obj.following.add(following)
        print("Followed")

    @classmethod
    def unfollow(self):
        obj, create = cls.objects.get_or_create(user=user)
        obj.following.remove(following)
        print("Unfollowed")

    