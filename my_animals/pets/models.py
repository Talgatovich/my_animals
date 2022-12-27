from django.db import models


class Pet(models.Model):
    """Модель питомца"""

    name = models.CharField("Кличка", max_length=100)
    type = models.CharField("Вид животного", max_length=50)
    birth_year = models.IntegerField("Год рождения")
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
    pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name="photos"
    )

    class Meta:
        ordering = ("-pk",)
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        print(self.__dict__)
        print(self.image.__dict__)
        return self.image.name
