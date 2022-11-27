from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status, permissions
from get_outside.serializers.serializers import MappointSerializer
from django.contrib.auth.models import User
from get_outside.models.mappointModel import Mappoint
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated


# ViewSets define the view behavior.
class MappointViewSet(APIView):
    def detail_view(self, pk):
        try:
            return Mappoint.objects.get(pk=pk)
        except Mappoint.DoesNotExist:
            return Response(MappointSerializer.errors, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None, format=None):
        if id:
            data = self.detail_view(pk)
            serializer = MappointSerializer(data)
        else:
            data = Mappoint.objects.all()
            serializer = MappointSerializer(data, many=True)

        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def post(self, request, format='json'):
        data_request = JSONParser().parse(request)
        serializer = MappointSerializer(data=data_request)
        if serializer.is_valid():
            activity = serializer.save()
            if activity:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @permission_classes([IsAuthenticated])
    def put(self, request, pk, format='json'):
        object = Mappoint.objects.get(pk=pk)
        data_request = JSONParser().parse(request)
        # Passing partial will allow us to update without passing the entire Todo object
        serializer= MappointSerializer(instance = object, data=data_request, partial=True)
        if serializer.is_valid():
            activity = serializer.save()
            if activity:
                json = serializer.data
                return Response(json, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def delete(self, pk, format='json'):
        deleteItem = Mappoint.objects.get(pk=pk)
        deleteItem.delete()
        return Response(
          #  'message': 'Todo Deleted Successfully',
            status=status.HTTP_200_OK)
