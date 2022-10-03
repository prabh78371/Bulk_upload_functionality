from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'images',blank = True)
    img =  models.ImageField(upload_to = 'images',blank = True)
    gst = models.IntegerField()
    amount = models.IntegerField()
    brand = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

