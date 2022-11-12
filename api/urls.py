from django.urls import path
from .views import TransformView

urlpatterns = [
    path("transform/", TransformView.as_view()),
]
