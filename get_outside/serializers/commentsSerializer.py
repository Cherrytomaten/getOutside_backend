from get_outside.models.commentsModel import Comment
from rest_framework import serializers

# Serializers define the API representation.
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['mappoint_id', 'author_id', 'created_at', 'text']
