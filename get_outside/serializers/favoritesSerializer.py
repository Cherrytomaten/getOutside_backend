from get_outside.models.favoritesModel import FavoritePins
from get_outside.serializers.serializers import MappointSerializer
from rest_framework import routers, serializers, viewsets
from authentication.serializers import UserSerializer


#class TimelineCommentSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = TestMappoint
   #     fields = "__all__"


class FavoritePinSerializer(serializers.ModelSerializer):
    #mappoint = TimelineCommentSerializer(many=True)

    class Meta:
        model = FavoritePins
        fields = ["title", "user"]
