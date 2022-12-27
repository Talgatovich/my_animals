# Generated by Django 4.1.4 on 2022-12-27 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pet",
            name="photos",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="pets.image",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="pet",
            name="birthday",
            field=models.DateField(verbose_name="День рождения"),
        ),
        migrations.DeleteModel(
            name="PetImage",
        ),
    ]
