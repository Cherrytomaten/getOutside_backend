import uuid
from random import randrange

from django.db import models
from authentication.models import CustomUser
from get_outside.models.mappointModel import Mappoint


def key_generator():
    key = randrange(100, 100000)
    if CustomUser.objects.filter(id=key).exists():
        key = key_generator()
    return key


# favorite list of pins
class FavoritePins(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #id = models.IntegerField(primary_key=True, default=key_generator, unique=True)
    pin = models.ForeignKey(Mappoint, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
