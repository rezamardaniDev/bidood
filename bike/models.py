from django.db import models

# Create your models here.
class Type(models.Model):
    type_name = models.CharField(max_length=250)
    type_slug = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'نوع'
        verbose_name_plural = 'دسته بندی'

    def __str__(self):
        return self.type_name

class Bike(models.Model):
    price = models.IntegerField(verbose_name='نرخ اجاره ساعتی')
    add_date = models.DateField(auto_now_add=True, verbose_name='تاریخ اضافه شدن')
    status = models.BooleanField(default=False, verbose_name='اجاره داده شده')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='نوع')

    class Meta:
        verbose_name = "دوچرخه"
        verbose_name_plural = "دورچرخه ها"

    def __str__(self):
        return f"{self.id} - {'اجاره داده شده' if self.status else 'اجاره داده نشده'}"