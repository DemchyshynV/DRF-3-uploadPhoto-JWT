from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from .models import CarModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
