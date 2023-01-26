from rest_framework import routers, serializers, viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.db.models import Avg
from django.shortcuts import get_object_or_404

from get_outside.models.mappointModel import Images, Mappoint, Ratings
from get_outside.serializers.serializers import ImageSerializer, MappointSerializer, RatingSerializer


# ViewSets define the view behavior.
class MappointViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def detail_view(self, pk):
        try:
            return get_object_or_404(Mappoint, pk=pk)
        except Mappoint.DoesNotExist:
            return Response(MappointSerializer.errors, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.detail_view(pk)
            serializer = MappointSerializer(data)
        else:
            data = Mappoint.objects.all()
            serializer = MappointSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format='json'):
        data_request = JSONParser().parse(request)
        serializer = MappointSerializer(data=data_request)
        if serializer.is_valid():
            point = serializer.save(creator_id=self.request.user.id)
            if point:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class RatingViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        # es wird übergeben: rating, mappoint_id und user_id
        data_request = JSONParser().parse(request)
        serializer = RatingSerializer(data=data_request)
        if serializer.is_valid():
            value = serializer.save()
            if value:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response(json, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        # pk = id vom Mappoint
        if pk:  
            try:
                average = Ratings.objects.all().filter(mappoint=pk).aggregate(Avg('rating'))
                print(average)
                return Response(average, status=status.HTTP_200_OK)
            except Ratings.DoesNotExist:
                return None
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        # pk = id vom Rating selber
        rating = get_object_or_404(Ratings, pk=pk)
        ratingCreator = rating.creator
        user_id = self.request.user.id
        if user_id == ratingCreator:
            rating.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
