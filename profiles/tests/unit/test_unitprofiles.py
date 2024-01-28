import pytest
from django.contrib.auth.models import User
from profiles.models import Profile
from django.test import Client
from django.urls import reverse
from unittest.mock import Mock

@pytest.fixture
def mock_user(mocker):
    return mocker.Mock(spec=User, username='testuser')

@pytest.fixture
def mock_profile():
    profile = Mock(spec=Profile)
    profile.user.username = 'testuser'
    profile.favorite_city = 'Test City'
    return profile

@pytest.fixture
def mock_profiles_list(mocker, mock_profile):
    return mocker.patch('profiles.models.Profile.objects.all', return_value=[mock_profile])

@pytest.fixture
def client():
    return Client()

def test_index_view_with_mocker(client, mock_profiles_list):
    response = client.get('http://127.0.0.1:8000/profiles/')  

    assert response.status_code == 200
    assert 'profiles/index.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_profile_view_with_mocker(client, mocker, mock_profile):    
    mocker.patch.object(Profile.objects, 'get', return_value=mock_profile)
    url = reverse('profiles:profile', kwargs={'username': 'testuser'})
    response = client.get(url)
    assert response.status_code == 200
    assert 'profiles/profile.html' in [t.name for t in response.templates]
    



#def test_dummy():
    #assert 1