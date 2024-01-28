from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Product, Weight
from django.db.models import F, Q


def add_product_to_recipe(request):
    """
    Функция добавляет к указанному рецепту указанный продукт с указанным весом.
    Если в рецепте уже есть такой продукт, то функция должна поменять его вес в этом рецепте на указанный.
    :param request:
    :return: HttpResponse
    """
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')
    if Weight.objects.filter(recipe__id=recipe_id, product__id=product_id).exists():
        (Weight.objects.filter(recipe__id=recipe_id, product__id=product_id).
         update(weight=F('weight') + float(weight)))
    else:
        product = Product.objects.get(id=product_id)
        recipe = Recipe.objects.get(id=recipe_id)
        Weight.objects.create(recipe=recipe, product=product, weight=weight)
    return HttpResponse("Product added to recipe successfully")


def cook_recipe(request):
    """
     Функция увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт.
    :param request:
    :return: HttpResponse
    """
    recipe_id = request.GET.get('recipe_id')
    recipe = Recipe.objects.prefetch_related('products').get(pk=recipe_id)
    Product.objects.filter(id__in=recipe.products.values_list('id')).update(usages=F('usages') + 1)
    return HttpResponse("Recipe cooked successfully")


def show_recipes_without_product(request):
    """
    Функция возвращает HTML страницу, на которой размещена таблица. В таблице отображены id и названия всех рецептов,
     в которых указанный продукт отсутствует, или присутствует в количестве меньше 10 грамм
    :param request:
    :return: HttpResponse
    """
    product_id = request.GET.get('product_id')
    recipes_without_product = Recipe.objects.filter(~Q(products__id__contains=product_id))
    recipes_with_product = Weight.objects.filter(Q(product__id=product_id) & Q(weight__lt=10))
    return render(request, 'recipes.html',
                  {'recipes_without_product': recipes_without_product,
                   'recipes_with_product': recipes_with_product})
