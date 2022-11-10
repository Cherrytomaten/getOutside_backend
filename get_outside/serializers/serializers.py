from rest_framework import serializers

""" from django.contrib.auth.models import User """

from get_outside.models import activityModel, categoryModel


""" # Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff') """

# Serializers define the API representation.
class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = activityModel
        fields = ('id','title', 'activity_id', 'category','created')

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = categoryModel
        fields = ('id','name')
