from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from authentication.models import CustomUser
from get_outside.models.mappointModel import Mappoint
from get_outside.models.presenceModel import Presence
from get_outside.serializers.presenceSerializer import PresenceSerializer
from get_outside.serializers.serializers import MappointSerializer
from django.shortcuts import get_object_or_404


class PresenceView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):  # add pin to list from loggedin user
        end_at = request.data['end_at']
        pin = request.data['pin']
        x = request.data['number']
        print("anzahl = " + x)
        for _ in range(x):
            data = {
                'end_at': end_at,
                'pin': pin
            }
            serializer = PresenceSerializer(data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=400)
        add_to_Mappoint(pin)
        return Response(serializer.data, status=201)
        print(serializer.errors)
        return Response(serializer.errors, status=400)


def add_to_Mappoint(pin):
    print('add mapponit visitors')
    count = Presence.objects.filter(pin=pin).count()
    print(count)
    mappoint = get_object_or_404(Mappoint, pk=pin)
    data = {
      'visitor': count
    }
    serializer = MappointSerializer(instance=mappoint, data=data, partial=True)
    if serializer.is_valid():
        activity = serializer.save()
        if activity:
            json = serializer.data
        return
