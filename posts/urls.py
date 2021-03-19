from django.urls import path
from posts.views import index

urlpatterns = [
    path('<int:pid>/', index, name="index"),
]