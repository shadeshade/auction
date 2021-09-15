from django.conf import settings
from django.db import models
from django.utils import timezone

from .tools import ResizeImageMixin


class BiddingItem(models.Model, ResizeImageMixin):
    item_name = models.CharField(
        max_length=150,
        unique=False,
        blank=False,
        null=False
    )
    image = models.ImageField(
        upload_to='item_images',
        default='item_images/default.jpg'
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        default=0
    )
    created_at = models.DateTimeField(
        null=False,
        default=timezone.now,
        editable=False
    )
    updated_at = models.DateTimeField(
        null=False,
        default=timezone.now,
        editable=False
    )
    auction_starts_at = models.DateTimeField(
        null=False,
        default=timezone.now,
        editable=True
    )
    auction_ends_at = models.DateTimeField(
        null=False,
        default=timezone.now,
        editable=True
    )
    seller = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='added_items',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    purchaser = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='purchased_items',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_sold = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.pk} - {self.item_name}'

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.resize(self.image, (600, 600))
        super().save(*args, **kwargs)
