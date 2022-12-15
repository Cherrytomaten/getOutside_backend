from django.urls import path

from get_outside.views import commentsView

urlpatterns = [
    path('mappoint/details/comments', commentsView.CommentsViewSet.as_view(), name='comment'),
    path('mappoint/details/comments/<pk>', commentsView.CommentsViewSet.as_view())
]
