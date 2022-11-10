from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from get_outside.serializers import ActivitieSerializer, CategorySerializer
from django.contrib.auth.models import User
from get_outside.models.activitiesModel import Activities, Category

# Create your views here.

""" # ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer """

# ViewSets define the view behavior.
class ActivitiesViewSet(viewsets.ModelViewSet):
    queryset = Activities.objects.all()
    serializer_class = ActivitieSerializer


# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
