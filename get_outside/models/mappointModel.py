import os
import uuid
from random import randrange

from django.db import models

from authentication.models import CustomUser
from Backend import settings


def key_generator():
    key = randrange(100, 100000)
    if CustomUser.objects.filter(id=key).exists():
        key = key_generator()
    return key


def upload_to(instance, filename):
    return 'mappoint/{filename}'.format(filename=filename)


class Mappoint(models.Model):
    CHOICES = (
        ('Outdoor', 'Outdoor Activity'),
        ('Indoor', 'Indoor Activity'),
        ('Out & In', 'Outdoor and Indoor Activity'),
    )
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #id = models.IntegerField(primary_key=True, default=key_generator, unique=True)
    title = models.CharField(max_length=30)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True) #default=0
    address = models.TextField()
    created = models.DateTimeField(auto_now=True)
    # end = models.DateTimeField()
    notes = models.CharField(choices=CHOICES, max_length=100, default='Outdoor')
    openingHours = models.JSONField(null=True)
    description = models.TextField()
    # picture = models.TextField()  # base64 string
    longitude = models.FloatField(max_length=10)
    latitude = models.FloatField(max_length=10)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]


class Images(models.Model):
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    mappoint = models.ForeignKey('Mappoint',
                                 related_name='image',
                                 on_delete=models.CASCADE, )

    def __str__(self):
        # return the id
        return self.id

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super(Images, self).delete(*args, **kwargs)

class Ratings(models.Model):
    rating = models.IntegerField(blank=True, null=True,)
    mappoint = models.ForeignKey('Mappoint', related_name='rating', on_delete=models.CASCADE,)
    creator_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.id