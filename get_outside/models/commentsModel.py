from django.db import models
from authentication.models import CustomUser
from get_outside.models.mappointModel import Mappoint

class Comment(models.Model):

    mappoint_id = models.ForeignKey(Mappoint, related_name='comments', default=0, on_delete= models.CASCADE)
    author_id = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE) # oder SET() ???
    created_at = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.text
