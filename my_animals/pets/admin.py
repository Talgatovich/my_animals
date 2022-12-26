from django.contrib import admin

from .models import Image, Pet, PetImage


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type", "birthday", "created_at")
    list_display_links = ("name",)
    list_filter = ("name", "type", "birthday", "created_at")
    search_fields = (
        "id",
        "name",
        "birthday",
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image")


@admin.register(PetImage)
class PetImageAdmin(admin.ModelAdmin):
    list_display = ("id", "pet", "image")
