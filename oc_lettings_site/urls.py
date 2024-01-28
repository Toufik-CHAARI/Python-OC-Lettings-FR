from django.contrib import admin
from django.urls import path, include
from . import views


def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path('sentry-debug/', trigger_error),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    #path('test-500/', views.test_500_error_view, name='test_500_error_view_name'),
]
