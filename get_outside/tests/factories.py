import factory
from get_outside.models.categoryModel import Category
# from get_outside.models.mappointModel import Mappoint

#Factory Module for model so we test our API’s with automatically generated dummy data

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")

# class MappointFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Mappoint

#     title= factory.Faker("title")
#     # category = models.ForeignKey("Category", on_delete=models.CASCADE)
#     address = factory.Faker("address")
#     created = factory.Faker("created")
#     #end = models.DateTimeField()
#     # notes = models.CharField(choices=CHOICES, max_length=100, default='Outdoor')
#     openingHours= factory.Faker("openingHours")
#     description = factory.Faker("description")
#     picture = factory.Faker("picture")
#     longitude = factory.Faker("longitude")
#     latitude= factory.Faker("latitude")
#     #creator_id=models.ForeignKey("User")
#     ratings= factory.Faker("ratings")
