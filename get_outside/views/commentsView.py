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
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format='json'):
        data_request=JSONParser().parse(request)
        print(request)
        serializer = CommentsSerializer(data=data_request)
        if serializer.is_valid():
            comment = serializer.save(author_id=self.request.user.id) #, mappointPin_id=self.request.??)   
            if comment:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        userCreatedComment = comment.author_id
        user_id = self.request.user.id
        if user_id == userCreatedComment:
            comment.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentsSerializer(comment, many=True)
        if comment:
            return Response(serializer.data)
        else:
            return HttpResponse("id not found / no authorization")
