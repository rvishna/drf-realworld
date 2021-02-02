"""Manager classes for the 'app_core' app."""
from typing import TYPE_CHECKING

from django.contrib.auth.base_user import BaseUserManager

if TYPE_CHECKING:  # pragma: no cover
    from conduit.core.models import User


class UserManager(BaseUserManager):
    """Manager class for the User model."""

    def create_user(self, email: str, password: str, **kwargs: str) -> "User":
        """Create a user with the given email and password."""
        email = self.normalize_email(email)
        user: "User" = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
