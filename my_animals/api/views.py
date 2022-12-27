from django.shortcuts import get_object_or_404
from pets.models import Pet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    LoadPhotoSerializer,
    PetCreateSerializer,
    PetShowSerializer,
)

OK = status.HTTP_200_OK
CREATED = status.HTTP_201_CREATED


class PetList(APIView):
    """Информация обо всех питомцах"""

    def get(self, request):
        pets = Pet.objects.all()
        serializer = PetShowSerializer(pets, many=True)
        return Response(serializer.data, status=OK)

    def post(self, request):
        serializer = PetCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=CREATED)

    # def delete(self, request):
    #
    #     pets_ids = request.data.values()
    #     result = {"deleted": 0, "errors": []}
    #     for val in pets_ids:
    #         try:
    #             current_pet = Pet.objects.get(pk=val)
    #             current_pet.delete()
    #             result["deleted"] += 1
    #         except Exception as error:
    #             err = {"id": val, "error": error}
    #             result["errors"].append(err)
    #     serializer = DeleteSerializer(result)
    #     return Response(serializer.data)


class PetDetail(APIView):
    """Вывод информации о конкретном питомце"""

    def get(self, request, pk):
        pet = get_object_or_404(Pet, pk=pk)
        serializer = PetShowSerializer(pet)
        return Response(serializer.data, status=OK)


class LoadPhoto(APIView):
    """Загрузка фотографии питомца"""

    def post(self, request, pk):
        request.data["pk"] = pk
        serializer = LoadPhotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=CREATED)
