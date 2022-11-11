from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status, permissions
from get_outside.serializers.serializers import ActivitySerializer
from django.contrib.auth.models import User
from get_outside.models.activityModel import Activity
from rest_framework.views import APIView
from rest_framework.response import Response

# ViewSets define the view behavior.
class ActivityViewSet(APIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer(queryset, many=True)

    def detail_view(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            return Response(ActivitySerializer.errors, status=status.HTTP_404_NOT_FOUND)


    def post(self, request, format='json'):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            activity = serializer.save()
            if activity:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format='json'):
        object = Activity.objects.get(pk=pk)

        # Passing partial will allow us to update without passing the entire Todo object
        serializer= ActivitySerializer(instance = object, data=request.data, partial=True)
        if serializer.is_valid():
            activity = serializer.save()
            if activity:
                json = serializer.data
                return Response(json, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format='json'):
        deleteItem = Activity.objects.get(pk=pk)
        deleteItem.delete()
        return Response(
          #  'message': 'Todo Deleted Successfully',
            status=status.HTTP_200_OK
        )
