from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='product')
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    
class News(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()