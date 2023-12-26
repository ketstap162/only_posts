from django.urls import path

from posts_app.views import index, create_post, delete_post, reply_post

app_name = "Post"

urlpatterns = [
    path("", index, name="home"),
    path("create/", create_post, name="create"),
    path("<int:pk>/delete", delete_post, name="delete"),
    path("<int:pk>/reply", reply_post, name="reply")
]
