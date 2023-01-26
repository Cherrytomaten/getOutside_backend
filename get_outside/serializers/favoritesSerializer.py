from get_outside.models.favoritesModel import FavoritePins
from get_outside.serializers.serializers import MappointSerializer
from rest_framework import serializers


class FavoritePinPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoritePins
        fields = '__all__'


class FavoritePinSerializer(serializers.ModelSerializer):
    pin = MappointSerializer()

    class Meta:
        model = FavoritePins
        fields = ["pin"]
