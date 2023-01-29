from django.contrib import admin
from authentication.models import CustomUser

from get_outside.models.mappointModel import Mappoint, Images
from get_outside.models.categoryModel import Category
from get_outside.models.favoritesModel import FavoritePins
from get_outside.models.commentsModel import Comment
from get_outside.models.RatingsModel import Ratings


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Mappoint)
admin.site.register(Images)
admin.site.register(Category)
admin.site.register(FavoritePins)
admin.site.register(Comment)
admin.site.register(Ratings)
