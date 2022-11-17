from django.test import TestCase, Client

# Create your tests here.

c = Client()
response = c.post('user/create', {'email': 'emilia.d@web.de', 'username': 'emilia', 'password': '12345678'})
response.status_code
""" response = c.get('/customer/details/')
response.content """
