from django.urls import path
from get_outside.views.activityView import  ActivityViewSet
from get_outside.views.categoryView import  CategoryViewSet

urlpatterns = [
   path('category', CategoryViewSet.as_view(), name='category'),
   path('create/category', CategoryViewSet.post.as_view()),
   path('categoryUpdate/<pk>', CategoryViewSet.put.as_view()),
   path('categoryDelete/<pk>', CategoryViewSet.delete.as_view()),
   path('categoryDetail/<pk>', CategoryViewSet.detail_view.as_view()),


   path('activity',ActivityViewSet.as_view(), name='activity'),
   path('create/activity', ActivityViewSet.post.as_view()),
   path('activityUpdate/<pk>', ActivityViewSet.put.as_view()),
   path('activityDelete/<pk>', ActivityViewSet.delete.as_view()),
   path('activityDetail/<pk>', ActivityViewSet.detail_view.as_view()),

]
