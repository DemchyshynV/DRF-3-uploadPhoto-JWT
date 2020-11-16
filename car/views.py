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
