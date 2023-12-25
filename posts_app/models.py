import os

from bleach import clean
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from posts_app.posts_settings import ALLOWED_IMAGE_EXTENSIONS
from posts_app.utils.model_utils import attachment_file_path, check_attachment_extensions


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
    attachment = models.FileField(
        null=True,
        default=None,
        upload_to=attachment_file_path
    )

    objects = models.Manager()

    @property
    def attachment_type(self):
        _, extension = os.path.splitext(self.attachment.path)
        if extension in ALLOWED_IMAGE_EXTENSIONS:
            print("image")
            return "image"
        elif extension in ALLOWED_IMAGE_EXTENSIONS:
            print("txt")
            return "txt"

    def clean_text(self):
        allowed_tags = ["a", "code", "i", "strong"]

        cleaned_text = clean(
            str(self.text),
            tags=allowed_tags,
        )

        return cleaned_text

    def save(self, *args, **kwargs):
        if self.attachment:
            check_attachment_extensions(str(self.attachment))

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
