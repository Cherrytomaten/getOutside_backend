from get_outside.models.presenceModel import Presence
from rest_framework import serializers


# Serializers define the API representation.
class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = '__all__'
