from django.urls import path

from posts_app.views import index, create_post

app_name = "Post"

urlpatterns = [
    path("", index, name="home"),
    path("create/", create_post, name="create"),
]
