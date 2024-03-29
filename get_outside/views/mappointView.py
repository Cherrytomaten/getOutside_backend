from rest_framework import routers, serializers, viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.db.models import Avg
from django.shortcuts import get_object_or_404

from get_outside.models.RatingsModel import Ratings
from get_outside.models.mappointModel import Images, Mappoint
from get_outside.serializers.serializers import ImageSerializer, MappointSerializer, RatingSerializer, \
    UploadImageSerializer, ImagePostSerializer


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
            point = serializer.save()
            if point:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format='json'):
        object = get_object_or_404(Mappoint, pk=pk)
        data_request = JSONParser().parse(request)
        # Passing partial will allow us to update without passing the entire Todo object
        serializer = MappointSerializer(instance=object, data=data_request, partial=True)
        if serializer.is_valid():
            activity = serializer.save()
            if activity:
                json = serializer.data
                return Response(json, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format='json'):
        deleteItem = get_object_or_404(Mappoint, pk=pk)
        deleteItem.delete()
        return Response(
            status=status.HTTP_200_OK)


class MappointImageView(APIView):
    permission_classes = (IsAuthenticated,)

    # get favorite list form loggedin user
    def get(self, request, *args, **kwargs):  
        print('Hallo')
        img = Images.objects.filter(user=request.user.uuid)  # favorites from that user
        serializer = ImageSerializer(img, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

 # add pin to list from loggedin user
    def post(self, request, *args, **kwargs): 
        pin_id = request.data.get('mappoint')  # pin id
        cloud_pic = request.data.get('cloud_pic')
        data = {
            'mappoint': pin_id,
            'cloud_pic': cloud_pic,
        }
        serializer = ImagePostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        print(serializer.errors)
        return Response(serializer.errors, status=400)

 # delete pin from list from loggedin user
    def delete(self, request, *args, **kwargs): 
        pin = request.data.get('mappoint')
        cloud_pic = request.data.get('cloud_pic')
        instance = Images.objects.filter(pin=pin, cloud_pic=cloud_pic)
        print(instance)
        if not instance:
            return Response({"res": "Object with id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)


class RatingViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, *args, **kwargs):  # pk = mappointid
        object = get_object_or_404(Mappoint, pk=pk)
        # es wird übergeben: rating, mappoint_id und user_id
        rating = request.data.get('rating')
        already_exists = Ratings.objects.filter(mappoint=object, creator=request.user)
        if rating > 5 or rating < 0:
            return Response({'err': 'rating not in the range of 0-5'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if already_exists:
            already_exists.delete()
        data = {
            'mappoint': pk,
            'rating': rating,
            'creator': request.user.uuid,
        }
        serializer = RatingSerializer(data=data)
        if serializer.is_valid():
            value = serializer.save()
            if value:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response(json, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        if pk:
            try:
                average = Ratings.objects.all().filter(mappoint=pk).aggregate(Avg('rating'))
                print(average)
                return Response(average, status=status.HTTP_200_OK)
            except Ratings.DoesNotExist:
                return None
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
