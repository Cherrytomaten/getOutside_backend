from rest_framework import serializers

""" from django.contrib.auth.models import User """
from ..models.categoryModel import Category
from ..models.mappointModel import Mappoint, Images
from ..models.RatingsModel import Ratings
from get_outside.serializers.commentSerializer import CommentsSerializer


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Images
        fields = ['id', 'image', 'mappoint']


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField()

    class Meta:
        model = Ratings
        fields = ['id', 'rating', 'mappoint', 'creator']


# Serializers define the API representation.
class MappointSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, required=False)
    ratings = RatingSerializer(many=True, required=False)
    image = ImageSerializer(many=True, required=False)

    class Meta:
        model = Mappoint
        fields =  '__all__'

    def create(self, validated_data):
        return Mappoint.objects.create(**validated_data)


# Serializers define the API representation.
class CategorySerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=200)

    class Meta:
        model = Category
        fields = '__all__' 

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance
