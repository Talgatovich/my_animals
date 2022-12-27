# Generated by Django 4.1.4 on 2022-12-27 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0003_remove_pet_photos_image_pet"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pet",
            name="birthday",
        ),
        migrations.AddField(
            model_name="pet",
            name="birth_year",
            field=models.IntegerField(default=2000, verbose_name="Год рождения"),
            preserve_default=False,
        ),
    ]
