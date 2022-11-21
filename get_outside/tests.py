from django.test import TestCase
from get_outside.models.categoryModel import Category

# Create your tests here.

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Basketball")
        Category.objects.create(name="Soccer")

    def compareCategory(self):
        basketball = Category.objects.get(name="Basketball")
        soccer = Category.objects.get(name="Soccer")
        self.assertEqual(basketball,soccer)

    def getCategory(self):
        Category.objects.all()
