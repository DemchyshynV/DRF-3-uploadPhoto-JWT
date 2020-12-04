import os

from django.db import models


class TagModel(models.Model):
    class Meta:
        db_table = 'tags'

    tag = models.CharField(max_length=20)


# Create your models here.
class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=20)
    year = models.IntegerField()
    photo = models.ImageField(upload_to=os.path.join('car', 'img'), default='', blank=True)
    tags = models.ManyToManyField(TagModel, related_name='car')
