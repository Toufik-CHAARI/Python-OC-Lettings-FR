import logging
from django.shortcuts import render, get_object_or_404
from sentry_sdk import capture_message
from profiles.models import Profile

logger = logging.getLogger(__name__)  # pragma: no cover


def index(request):
    """
    Display a list of all profiles from the database
    in the 'profiles/index.html' template .
    """

    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Display the details of a specific profile from
    the database and passes its details to the 'profiles/profile.html' template.
    The argument letting_id must be provided
    """
    try:  # pragma: no cover
        profile = Profile.objects.get(user__username=username)
        logger.info(f"Profile for user {username} fetched successfully")  # pragma: no cover
    except Profile.DoesNotExist:  # pragma: no cover
        logger.error(f"Profile for user {username} not found")  # pragma: no cover
        capture_message(
            f"Profile for user {username} not found", level="error"
        )  # pragma: no cover
        profile = get_object_or_404(Profile, user__username=username)  # pragma: no cover
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
