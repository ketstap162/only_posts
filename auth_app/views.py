from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register_view(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "registration/register.html", context)


# def profile_view(request):
#     if not request.user.is_authenticated:
#         return redirect("login")
#
#     return redirect("VPN:home")
