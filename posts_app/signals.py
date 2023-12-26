import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from posts_app.models import Post
from posts_app.posts_settings import ALLOWED_IMAGE_EXTENSIONS
from posts_app.utils.model_utils import process_image


@receiver(post_save, sender=Post)
def process_uploaded_image(sender, instance, **kwargs):
    if instance.attachment:
        _, extension = os.path.splitext(instance.attachment.path)
        if extension in ALLOWED_IMAGE_EXTENSIONS:
            process_image(instance.attachment.path)
