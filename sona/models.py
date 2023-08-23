from django.db import models

# Create your models here.

class contact2(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    number=models.CharField(max_length=12)
    message=models.CharField(max_length=255)
        