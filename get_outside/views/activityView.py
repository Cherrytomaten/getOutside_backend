from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status, permissions
from get_outside.serializers.serializers import ActivitySerializer
from django.contrib.auth.models import User
from get_outside.models.activityModel import Activity
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

# ViewSets define the view behavior.
class ActivityViewSet(APIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer(queryset, many=True)


    @api_view(['POST', 'GET'])
    def post(self, request, format='json'):
        data_request = JSONParser().parse(request)
        serializer = ActivitySerializer(data=data_request)
        if serializer.is_valid():
            activity = serializer.save()
            if activity:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityViewSet2(APIView):
    @api_view(['GET'])
    def detail_view(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            return Response(ActivitySerializer.errors, status=status.HTTP_404_NOT_FOUND)

    @api_view(['PUT', 'GET'])
    def put(self, request, pk, format='json'):
        object = Activity.objects.get(pk=pk)
        data_request = JSONParser().parse(request)
        # Passing partial will allow us to update without passing the entire Todo object
        serializer= ActivitySerializer(instance = object, data=data_request, partial=True)
        if serializer.is_valid():
            activity = serializer.save()
            if activity:
                json = serializer.data
                return Response(json, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['DELETE'])
    def delete(self, pk, format='json'):
        deleteItem = Activity.objects.get(pk=pk)
        deleteItem.delete()
        return Response(
          #  'message': 'Todo Deleted Successfully',
            status=status.HTTP_200_OK
        )
