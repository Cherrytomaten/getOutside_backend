from rest_framework import serializers


""" from django.contrib.auth.models import User """

from ..models.mappointModel import Mappoint
from ..models.categoryModel import Category


""" # Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff') """


# Serializers define the API representation.
class MappointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mappoint
        fields = '__all__'

    def create(self, validated_data):
        return Mappoint.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


# Serializers define the API representation.
class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)

    class Meta:
        model = Category
        fields = '__all__'     #fields = ['id','name']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
