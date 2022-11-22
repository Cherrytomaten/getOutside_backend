from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from get_outside.serializers import commentsSerializer
from rest_framework.decorators import api_view

from get_outside.models.commentsModel import Comment

queryset = Comment.objects.all()
# serializer_class = commentsSerializer
permission_classes = (permissions.AllowAny,)

# ViewSets define the view behavior.

class CommentsViewSet(APIView):
    queryset = Comment.objects.all()
    # serializer_class = commentsSerializer
    permission_classes = (permissions.AllowAny,)

    def post (self, request, format='json'):
        serializer = commentsSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save()
            if comment:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (request, id):
        comment = get_object_or_404(Comment, id = id)
        if comment:
            comment.delete()
        return HttpResponseRedirect("/")

    def update (self, request, id):
        comment = get_object_or_404(Comment, id = id)
        serializer = commentsSerializer(data=request.data)
        if comment:
            comment.text = serializer.text # sth so dass Text von Comment bearbeitet werden kann
        return HttpResponse("comment updated")

    def get (request, id):
        comment = get_object_or_404(Comment, id = id)
        if comment:
            return Response (comment)
        else:
            return HttpResponse("id not found / no authorization")
