"""Models for the 'core' app."""
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from conduit.core.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Class that represents the User model."""

    username = models.CharField(max_length=30, unique=True)
    bio = models.TextField()
    image = models.URLField()
    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    class Meta:  # noqa: D106
        verbose_name = _("user")
        verbose_name_plural = _("users")
