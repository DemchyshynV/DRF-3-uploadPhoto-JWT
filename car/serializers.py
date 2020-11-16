from rest_framework.exceptions import ValidationError
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

    def validate_photo(self, image):
        # 12 Mb
        MAX_FILE_SIZE = 12000000
        print(image.name)
        if image.size > MAX_FILE_SIZE:
            print(image.size)
            raise ValidationError("File size too big!")
