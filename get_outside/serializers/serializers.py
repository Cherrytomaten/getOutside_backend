from rest_framework import serializers

""" from django.contrib.auth.models import User """

from get_outside.models import activitiesModel

""" # Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff') """

# Serializers define the API representation.
class ActivitieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = activitiesModel.Activities
        fields = ('id','title', 'activity_id', 'category','created')

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = activitiesModel.Category
        fields = ('id','name')
