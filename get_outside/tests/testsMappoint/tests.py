# from django.test import TestCase, Client
# # from get_outside.models.mappointModel import Mappoint
# from rest_framework.test import APIClient
# import pytest

# client = APIClient()

# @pytest.mark.django_db
# def test_getMappoint(data):
#     response = client.get('/api/mappoint')
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_getDetailedMappoint(data):
#     response = client.get('/api/mappoint/1')
#     assert response.status_code == 200



# # class MappointTestCase(TestCase):
# #     model testing
# #     def setUp_firstMappoint(self):
# #         return Mappoint.objects.create(
# #             title="Sportplatz Wilmersdorf",
# #             category= self.setUp_soccer(),
# #             address= "Straße am Schoelerpark 39, 10715 Berlin",
# #             # created
# #             notes='Outdoor',
# #             # openingHours=
# #             description= 'Here u can play soccer & Co',
# #             picture='12435reweq',
# #             longitude= 13.3222878,
# #             latitude= 52.4839994,
# #             ratings= 4.5
# #             )

# #     def test_compareMappoint(self):
# #         first = self.setUp_firstMappoint()
# #         self.assertTrue(isinstance(first, Mappoint))
