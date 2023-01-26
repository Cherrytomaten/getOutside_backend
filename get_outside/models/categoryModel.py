from django.db import models


class Category(models.Model):  # Sportart
    id = models.CharField(primary_key=True, max_length=200, unique=True)

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # name = models.CharField(max_length=200, unique=True)
    # reporter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.id
