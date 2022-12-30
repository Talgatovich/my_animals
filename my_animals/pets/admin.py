from django.contrib import admin

from .models import Image, Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type", "birth_year", "created_at")
    list_display_links = ("name",)
    list_filter = ("name", "type", "birth_year", "created_at")
    search_fields = (
        "id",
        "name",
        "birth_year",
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "pet")


#
# @admin.register(PetImage)
# class PetImageAdmin(admin.ModelAdmin):
#     list_display = ("id", "pet", "image")
