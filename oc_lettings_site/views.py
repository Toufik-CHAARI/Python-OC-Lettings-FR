from django.shortcuts import render


def index(request):
    return render(request, "index.html")


# def test_500_error_view(request):
# raise Exception("Testing 500 Internal Server Error")
