from django.db import models

# Create your models here.

class IMAGES(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    photo = models.ImageField(upload_to='uploads/', blank=True)