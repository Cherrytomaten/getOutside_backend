from django.contrib.auth.models import AbstractUser
from django.db import models


# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'profile_pictures/{filename}'.format(filename=filename)


class CustomUser(AbstractUser):
    fav_activity = models.CharField(blank=True, max_length=120)
    profile_picture = models.ImageField(upload_to=upload_to, blank=True, null=True)
