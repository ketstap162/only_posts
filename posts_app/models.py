from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


# Create your models here.


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    replied = models.ForeignKey(
        to="self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None
    )

    class Meta:
        ordering = ["-created_at"]
