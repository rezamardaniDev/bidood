from django.db import models
from account.models import *
from bike.models import *
from django_jalali.db import models as jmodels


# Create your models here.
class BikeToUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, verbose_name='دوچرخه')
    status = models.BooleanField(default=False, verbose_name="پس داده شده/نشده")
    date = jmodels.jDateTimeField(auto_now_add=True, verbose_name="تاریخ رزرو")

    class Meta:
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزروها'

    def __str__(self):
        return f"{self.user.id} - {self.bike.id}"
