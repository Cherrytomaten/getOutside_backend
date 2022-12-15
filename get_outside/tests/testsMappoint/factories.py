# import factory
# from get_outside.models.mappointModel import Mappoint

# class MappointFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Mappoint

#     title= factory.Faker("title")
#     category = factory.Faker("Category") #, on_delete=models.CASCADE)
#     address = factory.Faker("address")
#     created = factory.Faker("created")
#     #end = models.DateTimeField()
#     notes = factory.Faker("notes") #  choices=CHOICES, max_length=100, default='Outdoor')
#     openingHours= factory.Faker("openingHours")
#     description = factory.Faker("description")
#     picture = factory.Faker("picture")
#     longitude = factory.Faker("longitude")
#     latitude= factory.Faker("latitude")
#     creator_id=factory.Faker("User")
#     ratings= factory.Faker("ratings")
