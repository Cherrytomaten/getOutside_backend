from django.test import TestCase, Client
from get_outside.models.categoryModel import Category
from rest_framework.test import APIClient
import pytest

# # Create your tests here.

# client = Client()
client = APIClient()

@pytest.mark.django_db
def test_getCategory(data):
    response = client.get('/api/category')
    assert response.status_code == 200

@pytest.mark.django_db
def test_getDetailedCategory(data):
    response = client.get('/api/category/1')
    assert response.status_code == 401


@pytest.mark.django_db
def test_postCategory():
    payload = {
       "name": "Soccer"
    }
    response = client.post('/api/category', payload, format='json')
    assert response.status_code == 201

@pytest.mark.django_db
def test_putCategory():
    payload = {
       "name": "Soccer"
    }
    payload2 = {
       "name": "Golf"
    }
    response = client.post('/api/category', payload, format='json')
    assert response.status_code == 201
    response2 = client.put('/api/category/1', payload2, format="json")
    assert response2.status_code == 401

# # @pytest.mark.django_db
# # def test_deleteCategory():
# #     payload = {
# #        "name": "Soccer"
# #     }
# #     response = client.post('/api/category', payload, format='json')
# #     assert response.status_code == 201
# #     response = client.put('/api/category/1', format='json')
# #     assert response.status_code == 200

# class CategoryTestCase(TestCase):
#     #model testing
#     def setUp_basketball(self):
#         return Category.objects.create(name="Basketball")

#     def setUp_soccer(self):
#         return Category.objects.create(name="Soccer")

#     def test_compareCategory(self):
#         basketball = self.setUp_basketball()
#         soccer = self.setUp_soccer()
#         self.assertNotEqual(basketball,soccer)
#         self.assertTrue(isinstance(basketball, Category))
#         self.assertTrue(isinstance(soccer, Category))
