from django.contrib.auth import get_user_model
from django.test import TestCase

from emobilis_crud.apps.users.models import UserProfile

User = get_user_model()

# Create your tests here.
class BaseModelTest(TestCase):
    """
    Test the Base Model
    """

    def setUp(self):
        self.user = User.objects.create(username="testuser", password="password")
        self.profile = UserProfile.objects.create(user=self.user,)

    def test_created_at_is_auto_set(self):
        self.assertIsNotNone(self.profile.created_at)

    def test_updated_at_is_auto_set(self):
        initial_updated_at = self.profile.updated_at
        self.profile.save()
        self.assertNotEqual(initial_updated_at, self.profile.updated_at)

    def test_is_active_defaults_to_true(self):
        self.assertTrue(self.profile.is_active)

    def test_deactivate(self):
        self.profile.deactivate()
        self.profile.refresh_from_db()
        self.assertFalse(self.profile.is_active)

    def test_activate(self):
        self.profile.activate()
        self.profile.refresh_from_db()
        self.assertTrue(self.profile.is_active)

