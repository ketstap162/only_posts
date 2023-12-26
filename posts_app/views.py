
from django.shortcuts import render, redirect

from http_utils.account_tools import login_required
from http_utils.errors import render_error_403_no_post_owner, render_error_404_no_post
from posts_app.forms import PostForm
from posts_app.models import Post
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    context = {
        "posts": Post.objects.filter(replied=None)
    }
    return render(request, "posts/posts.html", context=context)


@login_required
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


@login_required
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    if post.owner == request.user:
        post.delete()
        return redirect("Post:home")

    return render_error_403_no_post_owner(request)


@login_required
def reply_post(request, pk):
    try:
        reply_to = Post.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return render_error_404_no_post(request)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.replied = reply_to
            post.save()
            return redirect("Post:home")
    else:
        form = PostForm()

    return render(request, "posts/post-create.html", {"form": form, "reply_to": reply_to})
