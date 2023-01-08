from datetime import datetime as dt

from django.shortcuts import get_object_or_404
from pets.models import Image, Pet
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    """Вывод фотографии"""

    url = serializers.ImageField(source="image")

    class Meta:
        model = Image
        fields = ("id", "url")


class LoadPhotoSerializer(serializers.ModelSerializer):
    """Загрузка фотографии"""

    class Meta:
        model = Image
        fields = ("image",)

    def create(self, validated_data):
        data = self._kwargs["data"]
        image = data["image"]
        pet = get_object_or_404(Pet, pk=data["pk"])

        return Image.objects.create(image=image, pet=pet)

    def to_representation(self, instance):
        return ImageSerializer(instance).data


class PetShowSerializer(serializers.ModelSerializer):
    """Вывод информации о питомцах"""

    photos = ImageSerializer(many=True, read_only=True)
    age = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = ("id", "name", "age", "type", "photos", "created_at")

    def get_age(self, obj):
        return dt.now().year - obj.birth_year


class PetCreateSerializer(serializers.ModelSerializer):
    """Создание питомца"""

    class Meta:
        model = Pet
        fields = ("name", "type", "birth_year")

    def validate_birth_year(self, value):
        """Валидация года рождения"""
        year = dt.now().year
        if not (year - 40 < value <= year):
            raise serializers.ValidationError("Проверьте год рождения!")
        return value

    def to_representation(self, instance):
        data = PetShowSerializer(instance).data
        return data


class ShowImageSerializer(serializers.Serializer):
    """Вспомогательный сериализатор. Используется в ImageCLISerializer"""

    image = serializers.CharField(max_length=500)


class ImageCLISerializer(serializers.ModelSerializer):
    """Сериализатор для вывода фото в консоль"""

    class Meta:
        model = Image
        fields = ("image",)

    def to_representation(self, instance):
        data = ShowImageSerializer(instance).data["image"]
        return data


class CLISerializer(serializers.ModelSerializer):
    """Вывод информации о питомцах в консоль"""

    photos = ImageCLISerializer(many=True, read_only=True)
    age = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = ("id", "name", "age", "type", "photos", "created_at")

    def get_age(self, obj):
        return dt.now().year - obj.birth_year
