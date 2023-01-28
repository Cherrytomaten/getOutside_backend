from get_outside.models.commentsModel import Comment
from rest_framework import serializers
# from ..serializers.serializers import MappointSerializer

# Serializers define the API representation.
class CommentsSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=255)
    # mappoint= MappointSerializer(required=False)

    class Meta:
        model = Comment
        fields = ['author', 'text', 'created_at']