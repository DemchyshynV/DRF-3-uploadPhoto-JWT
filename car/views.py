from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import CarSerializer, UserSerializer
from .models import CarModel


class ListCreateView(ListModelMixin, CreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        data = UserSerializer(user).data
        print(user.__dict__)
        return Response(data)


class PhotoView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, *args, **kwargs):
        user = CarModel.objects.get(id=kwargs.get('pk'))
        print(self.request.FILES)
        serializer = CarSerializer(user, data=self.request.FILES, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response('saved')


import operator
from functools import reduce
from django.db.models import Q


class FilterView(APIView):

    def get(self, *args, **kwargs):
        params = self.request.query_params.copy()
        model = params.pop('model', [])
        params = params.items()
        obj = CarModel.objects.filter(*params)
        print(~reduce(operator.and_, [Q(tags__tag__exact=x) for x in model]))
        if model:
            obj = obj.exclude(~reduce(operator.and_, [Q(tags__tag__exact=x) for x in model]))
        data = CarSerializer(obj, many=True).data
        return Response(data, status=status.HTTP_200_OK)
