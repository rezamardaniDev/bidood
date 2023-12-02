from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=11, default='0', null=True, verbose_name='شماره تماس')

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"


    def __str__(self):
        return f"{self.first_name}{self.last_name}"