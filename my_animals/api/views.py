from pets.models import Image, Pet, PetImage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PetSerializer

OK = status.HTTP_200_OK


class APIPet(APIView):
    def get(self, request):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data, status=OK)
