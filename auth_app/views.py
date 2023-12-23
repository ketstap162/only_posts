from django.shortcuts import render, redirect

from auth_app.forms import CustomUserCreationForm


def register_view(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Post:home")

    context = {"form": form}
    return render(request, "registration/register.html", context)


# def profile_view(request):
#     if not request.user.is_authenticated:
#         return redirect("login")
#
#     return redirect("Post:home")
