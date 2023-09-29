from django.db import models

from emobilis_crud.apps.base.models import BaseModel
from emobilis_crud.apps.users.models import User

class UserProfile(BaseModel):
    """
    User Profile Model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
