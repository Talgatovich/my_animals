from django.urls import path

from .views import APIPet

urlpatterns = [
    path("pets/", APIPet.as_view()),
]
