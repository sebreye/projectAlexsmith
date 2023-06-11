from django.db import models

# Create your models here.
class Skills(models.Model):
    title_skills = models.CharField(max_length=50)
    lvl_skills = models.IntegerField()