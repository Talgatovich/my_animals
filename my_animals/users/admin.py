from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "date_joined",
    )
    search_fields = (
        "id",
        "first_name",
        "last_name",
        "email",
    )
    list_filter = (
        "id",
        "first_name",
        "last_name",
        "email",
    )
