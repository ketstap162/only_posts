from django.urls import path

from posts_app.views import index

app_name = "Post"

urlpatterns = [
    path("", index, name="home")
]
