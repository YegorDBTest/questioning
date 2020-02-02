from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ECONOMY = 'EC'
    MEDICINE = 'MD'
    IT = 'IT'
    OCCUPATIONS = (
        (ECONOMY, 'Экономика'),
        (MEDICINE, 'Медицина'),
        (IT, 'IT'),
    )

    age = models.PositiveIntegerField('Возраст', null=True)
    occupation = models.CharField('Род деятельности', choices=OCCUPATIONS, default=ECONOMY, max_length=2, null=True)
    facebook_username = models.CharField('Имя пользователя в Facebook', max_length=255, blank=True, null=True)


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        permissions = (
            ('showcase_allowed', 'Доступ к витрине'),
        )

    name = models.CharField('Название', max_length=255, unique=True)
    code = models.PositiveIntegerField('Код')
    price = models.DecimalField('Цена, руб.', max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'Заказ № {self.id}'
