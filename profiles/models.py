from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile in the database.
    Attributes:
        user (OneToOneField): A one-to-one relationship linking the profile to a Django User
        model instance.
        favorite_city (CharField): The user's favorite city, up to 64 characters. This field
        is optional.
    Methods:
        __str__: Returns a human-readable string representation of the profile, specifically
        the associated user's username.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
