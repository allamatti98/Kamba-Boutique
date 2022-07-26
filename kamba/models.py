from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length = 12)
    category = models.CharField(max_length = 10)
    price = models.IntegerField()
    description = models.CharField(max_length = 100)
    image_url = models.CharField(max_length = 2089)