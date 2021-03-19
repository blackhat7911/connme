from django.urls import path
from accounts.views import *

urlpatterns = [
    path('register/', registration_view, name="registration"),
    path('login/', login_view, name="login"),
]

