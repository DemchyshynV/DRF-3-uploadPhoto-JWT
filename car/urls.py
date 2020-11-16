from django.urls import path

from .views import ListCreateView, UserView, PhotoView

urlpatterns = [
    path('', ListCreateView.as_view()),
    path('user/', UserView.as_view()),
    path('photo/<int:pk>/', PhotoView.as_view())
]
