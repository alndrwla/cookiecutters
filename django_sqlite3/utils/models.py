from django.db import models

class CommonInfo(models.Model):
    created = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        blank=True,
        verbose_name="Date creation"
    )
    updated = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        blank=True,
        verbose_name="Date updated"
    )

    class Meta:
        abstract = True
