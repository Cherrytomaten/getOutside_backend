from django.db import models
from authentication.models import CustomUser
from django.conf import settings


class TestMappoint(models.Model):
    title = models.CharField(max_length=30)


# favorite list of pins
class FavoritePins(models.Model):
    title = models.ForeignKey(TestMappoint, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
