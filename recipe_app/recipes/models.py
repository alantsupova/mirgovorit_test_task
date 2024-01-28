from django.db import models


class Product(models.Model):
    """Модель продукта"""
    title = models.CharField(max_length=250, verbose_name='')
    usages = models.IntegerField(verbose_name='Кол-во использований в рецептах')
    
