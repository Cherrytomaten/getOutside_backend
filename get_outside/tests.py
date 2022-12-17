from django.test import TestCase
from models.commentsModel import Comment
from rest_framework.test import APIClient
import pytest

# Create your tests here.

class CommentTestCase(TestCase):
    #model testing
    def setUp_bfirstComment(self):
        return Comment.objects.create(comment_id = 1)

client = APIClient

@pytest.mark.django_db
def test_getComment(data):
    response = client.get('/api/mappoint/detail/comments/1')
    assert response.status_code == 200

@pytest.mark.django_db
def test_postComment(data):
    response = client.get('/api/mappoint/detail/comments')
    assert response.status_code == 200

@pytest.mark.django_db
def test_putComment(data):
    response = client.get('/api/mappoint/detail/comments/1')
    assert response.status_code == 200

@pytest.mark.django_db
def test_deleteCommand(data):
    response = client.get('/api/mappoint/detail/comments/1')
    assert response.status_code == 200
