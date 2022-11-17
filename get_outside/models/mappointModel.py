from django.db import models


class Mappoint(models.Model):
    CHOICES = (
        ('Outdoor', 'Outdoor Activity'),
        ('Indoor', 'Indoor Activity'),
        ('Out & In', 'Outdoor and Indoor Activity'),
    )
    title= models.CharField(max_length=30)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    address = models.TextField()
    created = models.DateTimeField(auto_now=True)
    #end = models.DateTimeField()
    notes = models.Choices(choices=CHOICES)
    openingHours= models.DateTimeField()
    description = models.TextField()
    picture = models.TextField() #base64 string
    longitude = models.FloatField()
    latitude= models.FloatField()
    #creator_id=models.ForeignKey("User")
    ratings= models.FloatField()



    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
