from django.http import HttpResponse
from django.shortcuts import render


def render_error(
        request,
        error_code: int = 500,
        error_message: str = "Sorry, an internal server error has occurred."
) -> HttpResponse:
    context = {
        "code": error_code,
        "message": error_message,
    }
    return render(request, "errors/http-error.html", context=context, status=error_code)


def render_error_403_no_post_owner(request):
    return render_error(
        request,
        error_code=403,
        error_message="Access is forbidden: You are not a post owner."
    )


def render_error_404_no_post(request):
    return render_error(
        request,
        error_code=404,
        error_message="Not Found: The post you want to reply to does not exist."
    )