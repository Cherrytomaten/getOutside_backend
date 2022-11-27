from django.test import TestCase
import unittest, json
from rest_framework.test import APIClient, APIRequestFactory
from .models import CustomUser
from selenium import webdriver
from django.urls import reverse



# Create your tests here.

client = APIClient()

class TestSignup(unittest.TestCase):
    def setUp(self):
        self.pravesh = CustomUser.objects.create(
        email='',
        username='',
        password='' )
        self.password = 'example password'
        self.pravesh.set_password(self.password)


    def test_method(self):
        client.login(email=self.pravesh.email, password=self.password)
        token = Token.objects.create(user= self.pravesh)
        response= client.post(
            reverse('account:post-data'),
            data = json.dumps(self.data),
            HTTP_AUTHORIZATION='Token {}'.format(token),
            content_type='aaplication/json'
        )
    def setUp(self):
        self.driver = webdriver.Chrome()
