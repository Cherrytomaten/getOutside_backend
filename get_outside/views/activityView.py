from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from get_outside.serializers.serializers import ActivitySerializer
from django.contrib.auth.models import User
from get_outside.models.activityModel import Activity
from rest_framework.views import APIView
# Create your views here.

# ViewSets define the view behavior.
class ActivityViewSet(APIView): #viewsets.ModelViewSet
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
