from django.db import models

# Create your models here.
class Restaurant(models.Model):
    title = models.CharField(max_length=200, default = "")
    description = models.CharField(max_length=280, default = "")
    address = models.CharField(max_length=280, default = "")
    cuisine = models.CharField(max_length=40, default = "")
    images = models.ImageField(upload_to='uploadedimages/', null=True, blank = True)