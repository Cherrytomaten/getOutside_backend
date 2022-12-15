from django.db import models
from authentication.models import CustomUser
# from get_outside.models import mappointModel

class Comment(models.Model):

    # CustomUser = userModel.CustomUser
    # mappoint = mappointModel

    # comment_id = models.CharField(max_length=255, blank=True)
    # mappoint_id = models.ForeignKey(mappoint, on_delete= models.CASCADE)
    author_id = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE) # oder SET() ???
    created_at = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.text
