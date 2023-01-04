import json
import os

from config.settings import BASE_DIR
from django.core.management.base import BaseCommand
from pets.models import Pet


class Command(BaseCommand):
    help = "Наполнение БД"

    def add_arguments(self, parser):
        parser.add_argument(
            "file_name", default="pets.json", nargs="?", type=str
        )

    def handle(self, *args, **options):
        f = open(
            os.path.join(os.path.join(BASE_DIR, "data"), options["file_name"]),
            "r",
            encoding="utf-8",
            errors="ignore",
        )
        pets = f.read()
        f.close()
        data = json.loads(pets)
        items = []
        if Pet.objects.count() == 0:
            for item in data:
                pet = Pet(
                    name=item["name"],
                    type=item["type"],
                    birth_year=item["birth_year"],
                )
                items.append(pet)
            Pet.objects.bulk_create(items)
            print("Данные успешно загружены!")
        else:
            print("Данные уже были загружены ранее!")
