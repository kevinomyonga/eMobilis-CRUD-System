from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """
    Base Model
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )
    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        abstract = True
