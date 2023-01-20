import math

from rest_framework import routers, serializers, viewsets, status, permissions
from get_outside.serializers.serializers import MappointSerializer, ImageSerializer
from django.contrib.auth.models import User
from get_outside.models.mappointModel import Mappoint, Images
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters import rest_framework as filters


# ViewSets define the view behavior.
class MappointViewSet(APIView):
    permission_classes = (AllowAny,)

    def detail_view(self, pk):
        try:
            return get_object_or_404(Mappoint, pk=pk)
        except Mappoint.DoesNotExist:
            return Response(MappointSerializer.errors, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None, format=None, lat=None, long=None, radius=None):
        if pk:
            data = self.detail_view(pk)
            serializer = MappointSerializer(data)
        else:
            if lat and long and radius:
                earth = 6378.137  #radius of the earth in kilometer
                pi = 3.14159
                m = (1 / ((2 * pi / 360) * earth)) / 1000  #1 meter in degree
                # var new_longitude = longitude + (your_meters * m) / cos(latitude * (pi / 180));
                long_threshold_west = long - (radius * m) / math.cos(lat * (pi/180))
                long_threshold_ost = long + (radius * m) / math.cos(lat * (pi /180))
                lat_threshold_north = lat + radius * m
                lat_threshold_south = lat - radius * m
                data = Mappoint.objects.all().filter(longitude__gte=long_threshold_west).filter(longitude__lte=long_threshold_ost).filter(latitude__lte=lat_threshold_north).filter(latitude__gte=lat_threshold_south)
                serializer = MappointSerializer(data, many=True)
            else:
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.data)

    def post(self, request, format='json'):
        data_request = JSONParser().parse(request)
        serializer = MappointSerializer(data=data_request)
        if serializer.is_valid():
            activity = serializer.save()
            if activity:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response(json, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin/ User?
    def put(self, request, pk, format='json'):
        object = get_object_or_404(Mappoint, pk=pk)
        data_request = JSONParser().parse(request)
        # Passing partial will allow us to update without passing the entire Todo object
        serializer= MappointSerializer(instance = object, data=data_request, partial=True)
        if serializer.is_valid():
            activity = serializer.save()
            if activity:
                json = serializer.data
                return Response(json, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request, pk, format='json'):
        deleteItem = get_object_or_404(Mappoint, pk=pk)
        deleteItem.delete()
        return Response(
          #  'message': 'Todo Deleted Successfully',
            status=status.HTTP_200_OK)


class UploadImage(APIView):
    queryset = Images.objects.all()
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk, *args, **kwargs):
        file = request.data['file']
        data = {
            'image': file,
            'mappoint': pk
        }
        serializer = ImageSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Images.objects.get(id=pk)
        except Images.DoesNotExist:
            return None

    def delete(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)

        if not instance:
            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
