from django.contrib import admin

from .models import Letting
from .models import Address

# Register the Letting and Address models in the Django admin site.

admin.site.register(Letting)
admin.site.register(Address)
