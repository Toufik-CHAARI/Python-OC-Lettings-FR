from django.test import TestCase
from lettings.models import Address, Letting
from django.core.exceptions import ValidationError
from django.db import IntegrityError

class AddressModelTest(TestCase):
    def test_field_max_values(self):
        address = Address(number=10000, zip_code=100000)
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_state_length(self):
        address = Address(state='ABC')
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_country_iso_code_length(self):
        address = Address(country_iso_code='US')
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_string_representation(self):
        address = Address(number=123, street='Main Street')
        self.assertEqual(str(address), '123 Main Street')
        
    def test_address_creation_all_fields(self):
        address = Address.objects.create(
            number=123, street='Main Street', city='Springfield',
            state='SP', zip_code=12345, country_iso_code='USA'
        )
        self.assertEqual(address.number, 123)
        

    def test_invalid_state_and_country_iso_code_length(self):
        address = Address(state='ABC', country_iso_code='US')
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_address_deletion(self):
        address = Address.objects.create(
            number=123, street='Main Street', city='Springfield',
            state='SP', zip_code=12345, country_iso_code='USA'
        )
        address_id = address.id
        address.delete()
        self.assertFalse(Address.objects.filter(id=address_id).exists())
 
        

class LettingModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123, street='Main Street', city='Springfield',
            state='SP', zip_code=12345, country_iso_code='USA'
        )

    def test_string_representation(self):
        letting = Letting.objects.create(title='Nice Place', address=self.address)
        self.assertEqual(str(letting), 'Nice Place')

    def test_letting_address_relationship(self):
        letting = Letting.objects.create(title='Nice Place', address=self.address)
        self.assertEqual(letting.address, self.address)
    def test_letting_creation_with_address(self):
        letting = Letting.objects.create(title='Nice Place', address=self.address)
        self.assertEqual(letting.address, self.address)

    def test_letting_deletion_address_persistence(self):
        letting = Letting.objects.create(title='Nice Place', address=self.address)
        letting_id = letting.id
        letting.delete()
        self.assertFalse(Letting.objects.filter(id=letting_id).exists())
        self.assertTrue(Address.objects.filter(id=self.address.id).exists())

    def test_letting_title_length_validation(self):
        long_title = 'a' * 257
        with self.assertRaises(ValidationError):
            Letting(title=long_title, address=self.address).full_clean()

    

    def test_string_representation(self):
        letting = Letting.objects.create(title='Nice Place', address=self.address)
        self.assertEqual(str(letting), 'Nice Place')
