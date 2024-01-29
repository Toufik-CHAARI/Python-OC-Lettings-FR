import pytest
from django.urls import reverse
from django.test import Client
from lettings.models import Letting, Address


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def create_address(db):
    return Address.objects.create(
        number=123,
        street="Test Street",
        city="Test City",
        state="TS",
        zip_code=12345,
        country_iso_code="TC",
    )


@pytest.fixture
def create_letting(db, create_address):
    return Letting.objects.create(title="Test Letting", address=create_address)


def test_index_view_integration(client, create_letting):
    url = reverse("lettings:index")
    response = client.get(url)

    assert response.status_code == 200
    assert "lettings/index.html" in [t.name for t in response.templates]
    assert create_letting in response.context["lettings_list"]


def test_letting_view_integration(client, create_letting):
    url = reverse("lettings:letting", kwargs={"letting_id": create_letting.id})
    response = client.get(url)

    assert response.status_code == 200
    assert "lettings/letting.html" in [t.name for t in response.templates]
    assert response.context["title"] == create_letting.title
    assert response.context["address"] == create_letting.address
