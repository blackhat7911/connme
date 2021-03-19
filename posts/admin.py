from django.contrib import admin
from posts.models import Post, Image

class PostImageAdmin(admin.StackedInline):
    model = Image

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Post

@admin.register(Image)
class PostImageAdmin(admin.ModelAdmin):
    pass
