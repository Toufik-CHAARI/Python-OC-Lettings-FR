from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents an address in the database.
    Attributes:
        number (PositiveIntegerField): The street number of the address, must be less than 9999.
        street (CharField): The name of the street, up to 64 characters.
        city (CharField): The city name, up to 64 characters.
        state (CharField): The state code, exactly 2 characters.
        zip_code (PositiveIntegerField): The zip code, must be less than 99999.
        country_iso_code (CharField): The country ISO code, exactly 3 characters.

    Methods:
        __str__: Returns a human-readable string representation of the address.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name_plural = "Address"


class Letting(models.Model):
    """
    Represents a letting in the database.
    Attributes:
        title (CharField): The title of the letting, up to 256 characters.
        address (OneToOneField): A one-to-one relationship linking the letting to its address.
    Methods:
        __str__: Returns a human-readable string representation of the letting.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
