from rest_framework import routers, serializers, viewsets, status, permissions
from get_outside.serializers.serializers import MappointSerializer
from django.contrib.auth.models import User
from get_outside.models.mappointModel import Mappoint
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny



# ViewSets define the view behavior.
class MappointViewSet(APIView):
    permission_classes = (AllowAny,)

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
