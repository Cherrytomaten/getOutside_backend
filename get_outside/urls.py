from django.urls import path
from get_outside.views.mappointView import  MappointViewSet
from get_outside.views.categoryView import  CategoryViewSet, CategoryViewSet2
from get_outside.views.commentsView import CommentsViewSet

urlpatterns = [
   path('category', CategoryViewSet.as_view(), name='category'),
   path('category/<pk>', CategoryViewSet2.as_view()),

   path('mappoint',MappointViewSet.as_view(), name='mappoint'),
   path('mappoint/<pk>', MappointViewSet.as_view()),

   path('mappoint/details/comments', CommentsViewSet.as_view(), name='comment'),
   path('mappoint/details/comments/<pk>', CommentsViewSet.as_view())
]
