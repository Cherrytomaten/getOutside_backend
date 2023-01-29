from django.db import models


class Category(models.Model):  # Sportart
    id = models.CharField(primary_key=True, max_length=200, unique=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.id
