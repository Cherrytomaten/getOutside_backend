from rest_framework import serializers
from ..models.mappointModel import Mappoint, Images
from ..models.categoryModel import Category
# from get_outside.serializers.commentSerializer import CommentsSerializer


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Images
        fields = ['id', 'image', 'mappoint']
        

# Serializers define the API representation.
class MappointSerializer(serializers.ModelSerializer):
    # comments = CommentsSerializer(many=True, required=False)
    image = ImageSerializer(many=True, required=False)

    class Meta:
        model = Mappoint
        fields = '__all__'

    def create(self, validated_data):
        return Mappoint.objects.create(**validated_data)


# Serializers define the API representation.
class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)

    class Meta:
        model = Category
        fields = '__all__'  # fields = ['id','name']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
