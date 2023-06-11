from django.db import models

# Create your models here.
class portfolio(models.Model):
    section= models.CharField(max_length=200)
    image= models.ImageField(upload_to='portfolio/', blank=True, null=True)