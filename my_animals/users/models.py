from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""

    username = models.CharField(
        "Имя пользователя", max_length=150, unique=True
    )
    password = models.CharField(max_length=150)
    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    email = models.EmailField("E-mail", max_length=254, unique=True)
    date_joined = models.DateTimeField("Дата регистрации", auto_now_add=True)

    class Meta:
        ordering = ["-pk"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.first_name, self.last_name

    def get_short_name(self):
        return self.first_name
