from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from bleach import clean

# Create your models here.
from posts_app.utils.models import attachment_file_path


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
    attachment = models.FileField(null=True, upload_to=attachment_file_path)

    def clean_text(self):
        allowed_tags = ["a", "code", "i", "strong"]

        cleaned_text = clean(
            str(self.text),
            tags=allowed_tags,
            attributes={"a": ["href", "title"]}
        )

        return cleaned_text

    class Meta:
        ordering = ["-created_at"]
