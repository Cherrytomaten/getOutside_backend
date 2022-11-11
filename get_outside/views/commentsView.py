from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.http import HttpResponse
from get_outside.models.commentsModel import Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View

class CommentsCreate (CreateView):
    model = Comment
    fields = ['mappoint_id', 'author_id', 'created_at', 'text', 'rating', 'image', 'video']

class CommentsGet (View):
    def get(self, request):
        comment = get_object_or_404(Comment, id = id)
        return HttpResponse(comment)

class CommentsUpdate (UpdateView):
    # specify the model you want to use
    model = Comment

    # specify the fields
    fields = ['text', 'rating', 'image', 'video']

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/"

class CommentsDelete (DeleteView):
    # specify the model you want to use
    model = Comment

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/"



# Create your views here.

""" # ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer """

# ViewSets define the view behavior.
"""
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

    def post_comment (self, request, format='json'):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save()
            if comment:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_comment (request, id):
        comment = get_object_or_404(Comment, id = id)
        if comment:
            comment.delete()
        return HttpResponseRedirect("/")

    def update_comment (self, request, id):
        comment = get_object_or_404(Comment, id = id)
        serializer = CommentsSerializer(data=request.data)
        if comment:
            comment.text = serializer.text # sth so dass Text von Comment bearbeitet werden kann
        return HttpResponse("comment updated")
"""
