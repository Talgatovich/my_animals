import json
from pprint import pprint

from api.serializers import CLISerializer
from django.core.management.base import BaseCommand
from pets.models import Pet


class Command(BaseCommand):
    help = "Print all pets"

    def add_arguments(self, parser):
        parser.add_argument(
            "--has-photos",
            type=bool,
            help="Наличие фото",
        )

    def handle(self, *args, **kwargs):
        has_photos = kwargs["has_photos"]

        if has_photos:
            queryset = Pet.objects.all().filter(photos__isnull=False)
        else:
            queryset = Pet.objects.all()

        serializer = CLISerializer(queryset, many=True)
        content = json.dumps(
            {"pets": list(serializer.data)},
            indent=4,
        )
        pprint(json.loads(content))
