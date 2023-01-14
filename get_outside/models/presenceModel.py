import uuid
from datetime import datetime

from django.db import models
from get_outside.models.mappointModel import Mappoint


def default_start_time():
    now = datetime.now()
    end = now.replace(hour=(now.hour + 1) % 24)
    return end


# favorite list of pins
class Presence(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    created_at = models.TimeField(default=datetime.now())
    end_at = models.TimeField(default=default_start_time)
    pin = models.ForeignKey(Mappoint, on_delete=models.CASCADE)
