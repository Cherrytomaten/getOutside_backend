from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status, permissions
from ..serializers.serializers import CategorySerializer
from django.contrib.auth.models import User
from ..models.categoryModel import Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
import json
from django.shortcuts import get_object_or_404

# ViewSets define the view behavior.
class CategoryViewSet(APIView):
# """     permission_classes = (IsAuthenticated,) """
    get_serializer= CategorySerializer

    def detail_view(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response(CategorySerializer.errors, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.detail_view(pk)
            serializer = CategorySerializer(data)
        else:
            data = Category.objects.all()
            serializer = CategorySerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format="json"):
        data_request = JSONParser().parse(request)
        #serializer = self.get_serializer(data=request)
        serializer = CategorySerializer(data=data_request)
        if serializer.is_valid():
            category = serializer.save()
            if category:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response(json, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @permission_classes([IsAuthenticated])
    def put(self, request, pk , format='json'):
        object = get_object_or_404(Category, pk=pk)
        data_request = JSONParser().parse(request)
        # Passing partial will allow us to update without passing the entire Todo object
        serializer= CategorySerializer(instance=object, data=data_request, partial=True)
        if serializer.is_valid():
            category = serializer.save()
            if category:
                json = serializer.data
                return Response(json, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk, format='json'):
        deleteItem = get_object_or_404(Category, pk=pk)
        deleteItem.delete()
        return Response(
          #  'message': 'Todo Deleted Successfully',
        status=status.HTTP_200_OK)
