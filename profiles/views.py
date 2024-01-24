from django.shortcuts import render
from profiles.models import Profile


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
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
