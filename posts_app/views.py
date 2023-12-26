from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from http_utils.account_tools import login_required
from http_utils.errors import render_error_403_no_post_owner, render_error_404_no_post
from posts_app.forms import PostForm
from posts_app.models import Post
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    posts = Post.objects.filter(replied=None)
    sort_order = request.GET.get("sort_by_date", 0)
    username_filter = request.GET.get("username_filter")

    if sort_order:
        posts = posts.order_by(f"{'' if sort_order == 'old' else '-'}created_at")

    if username_filter:
        posts = posts.filter(owner__username__startswith=username_filter)

    posts_per_page = int(request.GET.get("posts_per_page", 25))

    paginator = Paginator(posts, posts_per_page)
    page = request.GET.get("page")

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts
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
