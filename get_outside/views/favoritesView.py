from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from authentication.models import CustomUser
from get_outside.models.mappointModel import Mappoint
from get_outside.serializers.favoritesSerializer import FavoritePinSerializer, FavoritePinPostSerializer
from get_outside.models.favoritesModel import FavoritePins


class FavoritePinView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs): #get favorite list form loggedin user
        print('Hallo')
        favorites = FavoritePins.objects.filter(user=request.user.uuid)  # favorites from that user
        serializer = FavoritePinSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):#add pin to list from loggedin user
        pin_id = request.data.get('pin')  # pin id
        data = {
            'pin': pin_id,
            'user': request.user.uuid,
        }
        already_exists = FavoritePins.objects.filter(pin=request.data.get('pin'), user=request.user)
        if already_exists:
            return Response({"res": "Object already your favorite!"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = FavoritePinPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        print(serializer.errors)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs): #delete pin from list from loggedin user
        pin = request.data.get('pin')
        user = request.user.uuid
        instance = FavoritePins.objects.filter(pin=pin, user=user)
        print(instance)
        if not instance:
            return Response({"res": "Object with id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
