from django.shortcuts import render


def render_error(
        request,
        error_code: int = 500,
        error_message: str = "Sorry, an internal server error has occurred."
):
    context = {
        "code": error_code,
        "message": error_message,
    }
    return render(request, "errors/http-error.html", context=context)
