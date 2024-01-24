from django.shortcuts import render
from lettings.models import Letting


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
    Display the details of a specific Lettingfrom
    the database and passes its details to the 'lettings/letting.html' template.
    The argument letting_id must be provided
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
