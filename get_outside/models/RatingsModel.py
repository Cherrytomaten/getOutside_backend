from django.db import models

from authentication.models import CustomUser
from get_outside.models.mappointModel import Mappoint


class Ratings(models.Model):
    rating = models.IntegerField(blank=True, null=True, )
    mappoint = models.ForeignKey(Mappoint, related_name='ratings', on_delete=models.CASCADE, )
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)
