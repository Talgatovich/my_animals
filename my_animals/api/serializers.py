from datetime import datetime as dt

from pets.models import Image, Pet
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.ImageField(source="image")

    class Meta:
        model = Image
        fields = ("id", "url")


class PetSerializer(serializers.ModelSerializer):
    photos = ImageSerializer(many=True, read_only=True)
    age = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = ("id", "name", "age", "type", "photos", "created_at")

    def get_age(self, obj):
        return dt.now().year - obj.birth_year
