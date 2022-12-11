from django.http import JsonResponse
from rest_framework import status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import CustomUser
from get_outside.serializers.favoritesSerializer import FavoritePinSerializer
from get_outside.models.favoritesModel import FavoritePins

'''
class FavoritePinView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        favorites = FavoritePins.objects.all()
        # user_instance = request.user
        serializer = FavoritePinSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user_instance = request.user
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = FavoritePinSerializer(data=data)
        # check if the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=400)

    '''


class FavoritePinView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        favorites = FavoritePins.objects.filter(user=request.user.id)
        serializer = FavoritePinSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        #data = JSONParser().parse(request)
        data={
            'title': request.data.get('title'),
            'user': request.user.id
        }
        # instanciate with the serializer
        serializer = FavoritePinSerializer(data=data)
        # check if the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return Response(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        print(serializer.errors)
        return Response(serializer.errors, status=400)
