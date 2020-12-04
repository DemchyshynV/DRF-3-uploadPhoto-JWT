from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class PostModel(models.Model):
    class Meta:
        db_table = 'posts'

    title = models.CharField(max_length=20)
    body = models.CharField(max_length=20)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
