import pytest
from django.urls import reverse
from django.test import Client
from lettings.models import Letting,Address
from collections import namedtuple
from django.test import TestCase



@pytest.fixture
def client():
    return Client()

@pytest.fixture
def mock_letting(mocker):
    mock = mocker.Mock(spec=Letting)
    mock.id = int(1)
    mock.title = "Test Letting"
    mock.address = "123 Test Street"
    return mock

class LettingViewTestCase(TestCase):
    def setUp(self):        
        self.address1 = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TST"
        )
        self.address2 = Address.objects.create(
            number=456,
            street="Test Avenue",
            city="Test City",
            state="TS",
            zip_code=54321,
            country_iso_code="TST"
        )

        
        self.letting1 = Letting.objects.create(title="Test Letting 1", address=self.address1)
        self.letting2 = Letting.objects.create(title="Test Letting 2", address=self.address2)

    def test_index_view_with_mocker(self):
        
        url = reverse('lettings:index')
        response = self.client.get(url)

        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertEqual(len(response.context['lettings_list']), 2)

        
        for letting in response.context['lettings_list']:
            self.assertIsInstance(letting.id, int)  









'''
def test_index_view_with_mocker(client, mocker):
    # Create mock Letting objects with specific integer IDs
    mock_letting1 = mocker.Mock(spec=Letting, id=int(1), title="Test Letting 1", address="123 Test Street")
    mock_letting2 = mocker.Mock(spec=Letting, id=int(2), title="Test Letting 2", address="456 Test Avenue")

    # Patch Letting.objects.all() to return these mock objects
    mock_lettings_list = mocker.patch('lettings.models.Letting.objects.all')
    mock_lettings_list.return_value = [mock_letting1, mock_letting2]

    # Call the index view
    url = reverse('lettings:index')
    response = client.get(url)

    # Assertions
    assert response.status_code == 200
    assert 'lettings/index.html' in [t.name for t in response.templates]
    assert len(response.context['lettings_list']) == 2

    # Ensure the correct IDs are passed to the template
    #for letting in response.context['lettings_list']:
        #assert isinstance(letting.id, int)  # Check if ID is an integer
'''



def test_letting_view_with_mocker(client, mocker, mock_letting):
    
    mocker.patch('lettings.models.Letting.objects.get', return_value=mock_letting)

    url = reverse('lettings:letting', kwargs={'letting_id': mock_letting.id})
    response = client.get(url)

    assert response.status_code == 200
    assert 'lettings/letting.html' in [t.name for t in response.templates]
    assert response.context['title'] == mock_letting.title
    assert response.context['address'] == mock_letting.address
