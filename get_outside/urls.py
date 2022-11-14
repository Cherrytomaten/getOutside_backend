from django.urls import path
from get_outside.views.activityView import  ActivityViewSet, ActivityViewSet2
from get_outside.views.categoryView import  CategoryViewSet, CategoryViewSet2

urlpatterns = [
   path('category', CategoryViewSet.as_view(), name='category'),
   path('category/<pk>', CategoryViewSet2.as_view()),

   path('activity',ActivityViewSet.as_view(), name='activity'),
   path('activity/<pk>', ActivityViewSet2.as_view()),
]
