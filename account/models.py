from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_admin = models.BooleanField(
        default=False,
        help_text="Designates that this user has permissions to access all dashboard.",
        verbose_name="Admin"
    )
    is_doctor = models.BooleanField(
        default=False,
        help_text="Designates that this user has permissions to access doctor dashboard.",
        verbose_name="Doctor"
    )
    is_reception = models.BooleanField(
        default=False,
        help_text="Designates that this user has permissions to access reception dashboard.",
        verbose_name="Reception"
    )
