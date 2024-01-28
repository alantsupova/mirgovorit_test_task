from django.db import models


class Product(models.Model):
    """Модель продукта"""
    title = models.CharField(max_length=250, verbose_name='Название продукта')
    usages = models.IntegerField(verbose_name='Кол-во использований в блюдах')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Recipe(models.Model):
    """Модель рецепта"""
    title = models.CharField(max_length=250, verbose_name='Название рецепта')
    products = models.ManyToManyField(Product, verbose_name='Ингредиенты', related_name='recipe',
                                      through='Weight')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Weight(models.Model):
    """Модель, связывающая рецепт и продукт с добавлением веса продукта"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.DecimalField(verbose_name='Вес ингредиента в рецепте', max_length=5, decimal_places=2,
                                 max_digits=3)

    
