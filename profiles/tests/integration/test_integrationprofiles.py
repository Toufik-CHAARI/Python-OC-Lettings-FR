import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from profiles.models import Profile

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def create_user(db):
    return User.objects.create_user(username='testuser', password='12345')

@pytest.fixture
def create_profile(db, create_user):
    return Profile.objects.create(user=create_user, favorite_city='Test City')

@pytest.mark.django_db
def test_index_view_integration(client, create_profile):
    url = reverse('profiles:index')
    response = client.get(url)

    assert response.status_code == 200
    assert 'profiles/index.html' in [t.name for t in response.templates]
    assert create_profile in response.context['profiles_list']

@pytest.mark.django_db
def test_profile_view_integration(client, create_profile):
    url = reverse('profiles:profile', kwargs={'username': 'testuser'})
    response = client.get(url)

    assert response.status_code == 200
    assert 'profiles/profile.html' in [t.name for t in response.templates]
    assert response.context['profile'] == create_profile
