import django_filters
from django.db.models.aggregates import Count
from pets.models import Pet


class PetFilter(django_filters.FilterSet):
    has_photos = django_filters.NumberFilter(
        method="get_has_photos",
    )

    class Meta:
        model = Pet
        fields = ("has_photos",)

    def get_has_photos(self, queryset, name, value):
        if value == 1:
            return queryset.filter(photos.count == 0)
        return queryset
