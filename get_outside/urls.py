from django.urls import path
from rest_framework import routers
from get_outside.views.activitesView import ActivitiesViewSet, CategoryViewSet

urlpatterns = [

]

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/activities', ActivitiesViewSet)

router.register(r'api/category', CategoryViewSet)
