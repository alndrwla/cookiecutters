from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.models import CommonInfo

# Create your models here.


class CustomUser(CommonInfo, AbstractUser):
    ci = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="Ci"
    )

    def __str__(self):
        return self.ci

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-id"]
