from django.db import models
from authentication.models import CustomUser
from get_outside.models.mappointModel import Mappoint


# favorite list of pins
class FavoritePins(models.Model):
    pin = models.ForeignKey(Mappoint, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
