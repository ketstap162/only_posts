from django.shortcuts import render, redirect

# Create your views here.
from posts_app.forms import PostForm
from posts_app.models import Post


def index(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "posts/posts.html", context=context)


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect("Post:home")
    else:
        form = PostForm()

    return render(request, "posts/post-create.html", {"form": form})
