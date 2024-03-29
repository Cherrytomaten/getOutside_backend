from rest_framework import serializers

from ..models.categoryModel import Category
from ..models.mappointModel import Mappoint, Images
from ..models.RatingsModel import Ratings

from get_outside.serializers.commentSerializer import CommentsSerializer


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Images
        fields = ['id', 'image', 'mappoint', 'cloud_pic']


class ImagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'mappoint', 'cloud_pic']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'


# Serializers define the API representation.
class MappointSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, required=False)
    ratings = RatingSerializer(many=True, required=False)
    image = ImageSerializer(many=True, required=False)

    class Meta:
        model = Mappoint
        fields = '__all__'

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


class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["cloud_pic"]

    def update(self, instance, validated_data):
        instance.cloud_pic = validated_data['cloud_pic']
        instance.save()

        return instance
