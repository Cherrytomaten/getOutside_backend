from django.urls import path
from rest_framework import routers
from get_outside.views.activityView import  ActivityViewSet
from get_outside.views.categoryView import  CategoryViewSet

urlpatterns = [

]

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/activities', ActivityViewSet)

router.register(r'api/category', CategoryViewSet)
