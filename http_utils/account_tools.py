from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

login_required = login_required(login_url=reverse_lazy("login"))
