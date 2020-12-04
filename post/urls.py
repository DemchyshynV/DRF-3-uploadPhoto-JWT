from django.urls import path

from .views import PostView, PostUpdate
urlpatterns = [
    path('', PostView.as_view()),
    path('<int:pk>', PostUpdate.as_view())
]
