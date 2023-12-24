from django.db.models.signals import post_save
from django.dispatch import receiver
from posts_app.models import Post
from posts_app.utils.models import process_image


@receiver(post_save, sender=Post)
def process_uploaded_image(sender, instance, **kwargs):
    if instance.image:
        process_image(instance.image.path)
