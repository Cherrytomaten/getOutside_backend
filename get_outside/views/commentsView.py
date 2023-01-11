from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from get_outside.serializers.commentSerializer import CommentsSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from get_outside.models.commentsModel import Comment

# ViewSets define the view behavior.

class CommentsViewSet(APIView):
    # queryset = Comment.objects.all()
    # serializer_class = commentsSerializer
    
    permission_classes = (permissions.AllowAny,)
    # permission_classes = (permissions.IsAuthenticated,)


    def post(self, request, format='json'):
        data_request=JSONParser().parse(request)
        print(request)
        serializer = CommentsSerializer(data=data_request)
        if serializer.is_valid():
            comment = serializer.save(author_id=self.request.user.id) #, mappointPin_id=self.request.) 
                
            if comment:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response(
            status=status.HTTP_200_OK)

    def put(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentsSerializer(data=request.data)
        if comment:
            comment.text = serializer.text # sth so dass Text von Comment bearbeitet werden kann
        return HttpResponse("comment updated")
    #   serializer= MappointSerializer(instance = object, data=data_request, partial=True)
    #     if serializer.is_valid():
    #         activity = serializer.save()
    #         if activity:
    #             json = serializer.data
    #             return Response(json, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # comment = get_object_or_404(Comment, id = id)
        comment = Comment.objects.all()
        serializer = CommentsSerializer(comment, many=True)
        if comment:
            return Response(serializer.data)
        else:
            return HttpResponse("id not found / no authorization")
