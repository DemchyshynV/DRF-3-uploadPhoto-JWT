from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView

from .models import PostModel
from .serializers import PostSerializer


class PostView(ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        super().perform_create(serializer)


class PostUpdate(APIView):
    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        get = PostModel.objects.get(pk=pk)
        req = self.request.data
        # pop = req.pop('user')
        serializer = PostSerializer(get, data=req, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
