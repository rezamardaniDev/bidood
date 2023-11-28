from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    ...

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"


    def __str__(self):
        return f"{self.first_name}{self.last_name}"