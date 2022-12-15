from get_outside.models.categoryModel import Category
import factory

#Factory Module for model so we test our API’s with automatically generated dummy data

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")
