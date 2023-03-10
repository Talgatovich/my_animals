# Generated by Django 4.1.4 on 2023-01-05 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Кличка")),
                ("type", models.CharField(max_length=50, verbose_name="Вид животного")),
                ("birth_year", models.IntegerField(verbose_name="Год рождения")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Зарегистрирован"
                    ),
                ),
            ],
            options={
                "verbose_name": "Питомец",
                "verbose_name_plural": "Питомцы",
                "ordering": ("-pk",),
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to="pets/images/", verbose_name="Фото"),
                ),
                (
                    "pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="pets.pet",
                        verbose_name="Питомец",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фотография",
                "verbose_name_plural": "Фотографии",
                "ordering": ("-pk",),
            },
        ),
    ]
