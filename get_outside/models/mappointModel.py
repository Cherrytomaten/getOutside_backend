from django.db import models
from authentication.models import CustomUser


class Mappoint(models.Model):
    CHOICES = (
        ('Outdoor', 'Outdoor Activity'),
        ('Indoor', 'Indoor Activity'),
        ('Out & In', 'Outdoor and Indoor Activity'),
    )

    title= models.CharField(max_length=30)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    address = models.TextField()
    created = models.DateTimeField(auto_now=True)
    # end = models.DateTimeField()
    notes = models.CharField(choices=CHOICES, max_length=100, default='Outdoor')
    openingHours= models.JSONField(null=True)
    description = models.TextField()
    picture = models.TextField() #base64 string
    longitude = models.FloatField(max_length=10)
    latitude= models.FloatField(max_length=10)
    creator_id= models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    ratings= models.FloatField(max_length=20)



    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
