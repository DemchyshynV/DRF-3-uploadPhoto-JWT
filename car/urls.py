from django.urls import path

from .views import ListCreateView, UserView

urlpatterns = [
    path('', ListCreateView.as_view()),
    path('user/', UserView.as_view())
]
