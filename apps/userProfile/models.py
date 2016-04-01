from django.db import models

from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, related_name='profile')
    image = models.ImageField(upload_to='profile')
    birth_date = models.DateField()

