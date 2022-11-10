from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from get_outside.serializers.serializers import CategorySerializer
from django.contrib.auth.models import User
from get_outside.models.categoryModel import Category
from rest_framework.views import APIView

# ViewSets define the view behavior.
class CategoryViewSet(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
