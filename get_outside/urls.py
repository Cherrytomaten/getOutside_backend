from django.urls import path
from get_outside.views.mappointView import MappointViewSet, UploadImage, RatingViewSet
from get_outside.views.categoryView import CategoryViewSet, CategoryViewSet2
from get_outside.views.favoritesView import FavoritePinView

urlpatterns = [
    path('category', CategoryViewSet.as_view(), name='category'),
    path('category/<int:pk>', CategoryViewSet2.as_view()),

    path('mappoint', MappointViewSet.as_view(), name='mappoint'),
    path('mappoint/<int:pk>', MappointViewSet.as_view()),
    path('mappoint/upload/<int:pk>', UploadImage.as_view()),
    path('mappoint/rating/<int:pk>', RatingViewSet.as_view()),

    path('favorites/pin/', FavoritePinView.as_view(), name='favoritePin'),
]
