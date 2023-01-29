from get_outside.models.commentsModel import Comment
from rest_framework import serializers

# Serializers define the API representation.
class CommentsSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=255)

    class Meta:
        model = Comment
        fields = '__all__' #['author', 'text', 'created_at', 'mappointPin']