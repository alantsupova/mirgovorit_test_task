from django.db import models


class Product(models.Model):
    """Модель продукта"""
    title = models.CharField(max_length=250, verbose_name='Название продукта', unique=True)
    usages = models.IntegerField(verbose_name='Кол-во использований в блюдах', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Recipe(models.Model):
    """Модель рецепта"""
    title = models.CharField(max_length=250, verbose_name='Название рецепта')
    products = models.ManyToManyField(Product, verbose_name='Ингредиенты', related_name='recipe',
                                      through='Weight')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Weight(models.Model):
    """Модель, связывающая рецепт и продукт с добавлением веса продукта"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.FloatField(verbose_name='Вес ингредиента в рецепте')

    
