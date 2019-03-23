from django.db import models
from car_project.apps.core.models import TimeStampedModel


class Profile(TimeStampedModel):
    user =  models.OneToOneField("authentication.User", on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)
    def __str__(self):
        return self.user.username