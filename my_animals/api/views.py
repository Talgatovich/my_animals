import json

from django_filters import rest_framework as filters
from pets.models import Pet
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import PetFilter
from .serializers import (
    LoadPhotoSerializer,
    PetCreateSerializer,
    PetShowSerializer,
)

CREATED = status.HTTP_201_CREATED


class PetList(generics.ListCreateAPIView, generics.DestroyAPIView):
    """Информация обо всех питомцах"""

    queryset = Pet.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PetFilter

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PetShowSerializer
        return PetCreateSerializer

    def delete(self, request):
        result = {"deleted": 0, "errors": []}
        try:
            ids = json.loads(self.request.body.decode()).get("ids")
        except Exception:
            raise serializers.ValidationError("ids: [Обязательное поле.]")
        if ids is None:
            error = "Не введён ни один id"
            result["errors"].append(error)
            return Response(result)
        for pk in ids:
            try:
                current_pet = Pet.objects.all().get(pk=pk)
                current_pet.delete()
                result["deleted"] += 1
            except Exception:
                message = "Pet with the matching ID was not found"
                error = {"id": pk, "error": message}
                result["errors"].append(error)

        return Response(result)


class PetDetail(generics.RetrieveAPIView):
    """Вывод информации о конкретном питомце"""

    queryset = Pet.objects.all()
    serializer_class = PetShowSerializer


class LoadPhoto(APIView):
    """Загрузка фотографии питомца"""

    def post(self, request, pk):
        request.data["pk"] = pk
        serializer = LoadPhotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=CREATED)
