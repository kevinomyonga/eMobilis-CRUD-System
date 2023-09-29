from django.test import TestCase

from emobilis_crud.apps.students.models import Student

# Create your tests here.
class StudentModelTest(TestCase):
    """
    Test the Student Model
    """

    def setUp(self):
        self.student = Student.objects.create(name="test", email="test@email.com")

    def test_name_is_set(self):
        self.assertIsNotNone(self.student.name)
        self.assertEqual(self.student.name, "test")

    def test_email_is_set(self):
        self.assertIsNotNone(self.student.email)
        self.assertEqual(self.student.email, "test@email.com")
