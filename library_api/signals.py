from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Book


@receiver(post_save, sender=Book)
def invalidate_cache_on_update(sender, instance, **kwargs):
    # Invalidate the cache for the updated product
    cache_key = f"product_{instance.id}"
