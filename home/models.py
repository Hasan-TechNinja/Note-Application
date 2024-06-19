from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='product')
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    