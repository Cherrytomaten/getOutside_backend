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


class Comment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #id = models.IntegerField(primary_key=True, default=key_generator, unique=True)
    mappointPin = models.ForeignKey(Mappoint, related_name='comments', default=0, db_constraint=False, on_delete= models.CASCADE)
    author = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, db_constraint=False) 
    created_at = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.text
