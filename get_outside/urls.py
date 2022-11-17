from django.urls import path
from get_outside.views.mappointView import  MappointViewSet, MappointViewSet2
from get_outside.views.categoryView import  CategoryViewSet, CategoryViewSet2

urlpatterns = [
   path('category', CategoryViewSet.as_view(), name='category'),
   path('category/<pk>', CategoryViewSet2.as_view()),

   path('mappoint',MappointViewSet.as_view(), name='activity'),
   path('mappoint/<pk>', MappointViewSet2.as_view()),
]
