from django.db import models

class Category(models.Model): #Sportart

    name = models.CharField(max_length=200, unique=True)

    class Meta:
       ordering = ["name"]

    def __str__(self):
        return self.name