from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status, permissions
from get_outside.serializers.serializers import CategorySerializer
from django.contrib.auth.models import User
from get_outside.models.categoryModel import Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

# ViewSets define the view behavior.
class CategoryViewSet(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer() #queryset, many=True)
    # return Response(serializer_class.queryset)

    # def get(self, request, id=None, format=None):
    #     if id:
    #         data = self.detail_view(id)
    #         serializer = CategorySerializer(data)
    #     else:
    #         data = Category.objects.all()
    #         serializer = CategorySerializer(data, many=True)

    #         return Response(serializer.data)

    @api_view(['POST', 'GET'])
    def post(self, request, format='json'):
        data_request = JSONParser().parse(request)
        serializer = CategorySerializer(data=data_request)
        if serializer.is_valid():
            category = serializer.save()
            if category:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSet2(APIView):
    # @api_view(['GET'])
    # def detail_view(self, pk):
    #     try:
    #         return Category.objects.get(pk=pk)
    #     except Category.DoesNotExist:
    #         return Response(CategorySerializer.errors, status=status.HTTP_404_NOT_FOUND)

    @api_view(['PUT', 'GET'])
    def put(self, request,pk, format='json'): #request, id
        object = Category.objects.get(pk=pk)
        data_request = JSONParser().parse(request)
        # Passing partial will allow us to update without passing the entire Todo object
        serializer= CategorySerializer(instance = object, data=data_request, partial=True)
        if serializer.is_valid():
            category = serializer.save()
            if category:
                json = serializer.data
                return Response(json, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['DELETE'])
    def delete(self, request, pk, format='json'):
        deleteItem = Category.objects.get(pk=pk)
        deleteItem.delete()
        return Response(
          #  'message': 'Todo Deleted Successfully',
            status=status.HTTP_200_OK
        )
