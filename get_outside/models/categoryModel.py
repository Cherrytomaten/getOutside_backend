
from django.db import models
from authentication.models import CustomUser


class Category(models.Model):  # Sportart
    id = models.CharField(primary_key=True, max_length=200, unique=True)
    #name = models.CharField(max_length=200, unique=True)
    # reporter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.id
