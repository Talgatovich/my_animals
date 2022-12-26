from django.db import models


class Pet(models.Model):
    """Модель питомца"""

    name = models.CharField("Кличка", max_length=100)
    type = models.CharField("Вид животного", max_length=50)
    birthday = models.DateField("День рождения")
    created_at = models.DateTimeField("Зарегистрирован", auto_now_add=True)

    class Meta:
        ordering = ("-pk",)
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"

    def __str__(self):
        return self.name


class Image(models.Model):
    """Фото питомца"""

    image = models.ImageField(upload_to="pets/images/")

    class Meta:
        ordering = ("-pk",)
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return str(self.id)


class PetImage(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-pk",)
        verbose_name = "Фотография питомца"
        verbose_name_plural = "Фотографии питомцев"
