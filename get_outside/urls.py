from django.urls import path
from get_outside.views.mappointView import  MappointViewSet
from get_outside.views.categoryView import  CategoryViewSet

urlpatterns = [
   path('category', CategoryViewSet.as_view(), name='category'),
   path('category/<pk>', CategoryViewSet.as_view()),

   path('mappoint',MappointViewSet.as_view(), name='mappoint'),
   path('mappoint/<pk>', MappointViewSet.as_view()),
]
