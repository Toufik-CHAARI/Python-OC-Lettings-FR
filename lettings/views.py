from django.shortcuts import render
from lettings.models import Letting
import logging
from django.shortcuts import get_object_or_404
from sentry_sdk import capture_message

logger = logging.getLogger(__name__)  # pragma: no cover


def index(request):
    """
    Display a list of all Lettings from the database
    in the 'lettings/index.html' template .
    """
    lettings_list = Letting.objects.all()

    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Display the details of a specific Letting from
    the database and passes its details to the 'lettings/letting.html' template.
    The argument letting_id must be provided
    """
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logger.error(f"Letting with id {letting_id} not found")  # pragma: no cover
        capture_message(
            f"Letting with id {letting_id} not found", level="error"
        )  # pragma: no cover
        letting = get_object_or_404(Letting, id=letting_id)  # pragma: no cover

    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
