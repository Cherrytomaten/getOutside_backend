import os
import uuid

from django.db import models
# from django_filters import rest_framework as filters

from Backend import settings
from authentication.models import CustomUser


def upload_to(instance, filename):
    return 'mappoint/{filename}'.format(filename=filename)


class Mappoint(models.Model):
    CHOICES = (
        ('Outdoor', 'Outdoor Activity'),
        ('Indoor', 'Indoor Activity'),
        ('Out & In', 'Outdoor and Indoor Activity'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(max_length=30)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
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
    ratings = models.FloatField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]

'''
class RadiusFilter(filters.FilterSet):
    radiusLong = filters.NumberFilter(
        field_name='longitude', method='get_distance_for_longitude', label="dis_long")
    
    radiusLat = filters.NumberFilter(
        field_name='latitude', method='get_distance_for_latitude', label="dis_lat")

    def get_distance_for_longitude(self, queryset, field_name, value):

        time_threshold = timezone.now() - timedelta(hours=int(value))
        return queryset.filter(time_stamp__gte=time_threshold)

    class Meta:
        model = Mappoint
        fields = ('hours',)'''


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
