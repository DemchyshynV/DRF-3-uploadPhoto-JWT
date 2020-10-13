import os

from django.db import models


# Create your models here.
class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=20)
    year = models.IntegerField()
    photo = models.ImageField(upload_to=os.path.join('car', 'img'), default='', blank=True)
