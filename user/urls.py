from django.urls import path

from user.views import register_user

urlpatterns = [
    path("register_user", register_user, name="register_user")
]
