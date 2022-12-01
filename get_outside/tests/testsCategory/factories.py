import factory
from get_outside.models.categoryModel import Category

#Factory Module for model so we test our API’s with automatically generated dummy data

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")
