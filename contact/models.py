from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=200)