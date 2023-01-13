from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import CustomUser
from get_outside.serializers.favoritesSerializer import FavoritePinSerializer
from get_outside.models.favoritesModel import FavoritePins


class FavoritePinView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs): #get favorite list form loggedin user
        favorites = FavoritePins.objects.filter(user=request.user.id)  # favorites from that user
        serializer = FavoritePinSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):#add pin to list from loggedin user
        data = {
            'pin': request.data.get('pin'),  # pin id
            'user': request.user.id
        }

        already_exists = FavoritePins.objects.filter(pin=request.data.get('pin'), user=request.user.id)
        if already_exists:
            return Response({"res": "Object already your favorite!"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = FavoritePinSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        print(serializer.errors)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs): #delete pin from list from loggedin user
        pin = request.data.get('pin')
        user = request.user.id
        instance = FavoritePins.objects.filter(pin=pin, user=user)
        print(instance)
        if not instance:
            return Response({"res": "Object with id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
