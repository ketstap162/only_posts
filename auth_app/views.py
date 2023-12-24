from django.conf import settings
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect

from auth_app.forms import CustomUserCreationForm, CustomLoginForm


def register_view(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Post:home")

    context = {"form": form}
    return render(request, "registration/register.html", context)


def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                user = get_user_model().objects.get(email=email)
            except get_user_model().DoesNotExist:
                user = None

            if (user is not None) and check_password(password, user.password):
                login(request, user)
                return redirect("Post:home")
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = CustomLoginForm()

    return render(request, "registration/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return render(request, "registration/logged_out.html")
