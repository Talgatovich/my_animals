from django.db.models import Count
from django_filters import rest_framework as filters
from pets.models import Pet


class PetFilter(filters.FilterSet):
    has_photos = filters.BooleanFilter(
        method="get_has_photos",
    )

    class Meta:
        model = Pet
        fields = ("has_photos",)

    def get_has_photos(self, queryset, name, value):
        if value is True:
            return Pet.objects.annotate(count_photo=Count("photos")).filter(
                count_photo__gt=0
            )
        elif value is False:
            return Pet.objects.annotate(count_photo=Count("photos")).filter(
                count_photo__exact=0
            )
        return queryset
