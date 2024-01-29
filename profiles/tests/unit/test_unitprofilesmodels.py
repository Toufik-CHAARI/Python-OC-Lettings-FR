from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from django.core.exceptions import ValidationError
from django.db import IntegrityError


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")

    def test_profile_link_to_user(self):
        profile = Profile.objects.create(user=self.user, favorite_city="Springfield")
        self.assertEqual(profile.user, self.user)

    def test_favorite_city_max_length(self):
        profile = Profile(user=self.user, favorite_city="a" * 65)
        with self.assertRaises(ValidationError):
            profile.full_clean()

    def test_favorite_city_optional(self):
        profile = Profile.objects.create(user=self.user)
        self.assertEqual(profile.favorite_city, "")

    def test_string_representation(self):
        profile = Profile.objects.create(user=self.user, favorite_city="Springfield")
        self.assertEqual(str(profile), "testuser")

    def test_profile_creation_all_fields(self):
        profile = Profile.objects.create(user=self.user, favorite_city="Springfield")
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.favorite_city, "Springfield")

    def test_profile_deletion_cascade(self):
        profile = Profile.objects.create(user=self.user)
        self.user.delete()
        self.assertFalse(Profile.objects.filter(id=profile.id).exists())

    def test_duplicate_profile_for_user(self):
        Profile.objects.create(user=self.user)
        with self.assertRaises(IntegrityError):
            Profile.objects.create(user=self.user)

    def test_invalid_user_data_handling(self):
        with self.assertRaises(ValueError):
            Profile.objects.create(user="not_a_user_instance")

    def test_database_integrity(self):
        profile = Profile.objects.create(user=self.user, favorite_city="Metropolis")
        retrieved_profile = Profile.objects.get(id=profile.id)
        self.assertEqual(retrieved_profile.user, self.user)
        self.assertEqual(retrieved_profile.favorite_city, "Metropolis")
