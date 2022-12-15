from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from get_outside.serializers.commentsSerializer import CommentsSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from get_outside.models.commentsModel import Comment

# ViewSets define the view behavior.

class CommentsViewSet(APIView):
    # queryset = Comment.objects.all()
    # serializer_class = commentsSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        data_request=JSONParser().parse(request)
        serializer = CommentsSerializer(data=data_request)
        if serializer.is_valid():
            comment = serializer.save()
            if comment:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        comment = get_object_or_404(Comment, id = id)
        if comment:
            comment.delete()
        return HttpResponseRedirect("/")

    def put(self, request, id):
        comment = get_object_or_404(Comment, id = id)
        serializer = CommentsSerializer(data=request.data)
        if comment:
            comment.text = serializer.text # sth so dass Text von Comment bearbeitet werden kann
        return HttpResponse("comment updated")

    def get(self, request):
        # comment = get_object_or_404(Comment, id = id)
        comment = Comment.objects.all()
        serializer = CommentsSerializer(comment, many=True)
        if comment:
            return Response (serializer.data)
        else:
            return HttpResponse("id not found / no authorization")
