from django.db import models

from emobilis_crud.apps.base.models import BaseModel


def student_image_file_upload(instance, filename):
    return f"avatars/{filename}"

class Student(BaseModel):
    """
    Student Model
    """

    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    image = models.ImageField(upload_to=student_image_file_upload, blank=True, null=True,)
