from rest_framework import serializers

""" from django.contrib.auth.models import User """

from get_outside.models import categoryModel, mappointModel


""" # Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff') """

# Serializers define the API representation.
class MappointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = mappointModel
        fields = ('id','title', 'category', 'address', 'created', 'notes', 'openingHours',
         'description', 'picture', 'longitude', 'latitude', 'ratings')

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = categoryModel
        fields = ('id','name')
