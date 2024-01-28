from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Product, Weight
from django.db.models import F, Q


def add_product_to_recipe(request):
    '''
    Функция добавляет к указанному рецепту указанный продукт с указанным весом.
    Если в рецепте уже есть такой продукт, то функция должна поменять его вес в этом рецепте на указанный.
    :param request:
    :return: HttpResponse
    '''
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')
    recipe = Recipe.objects.prefetch_related('products').get(pk=recipe_id)
    product = Product.objects.get(pk=product_id)
    if recipe.products.filter(pk=product_id).exists():
        (Weight.objects.filter(recipe__id=recipe_id, product__id=product_id).
         update(weight=F('weight') + float(weight)))
    else:
        Weight.objects.create(recipe=recipe, product=product, weight=weight)
    return HttpResponse("Product added to recipe successfully")


def cook_recipe(request):
    '''
     Функция увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт.
    :param request:
    :return: HttpResponse
    '''
    recipe_id = request.GET.get('recipe_id')
    recipe = Recipe.objects.prefetch_related('products').get(pk=recipe_id)
    Product.objects.filter(id__in=recipe.products.values_list('id')).update(usages=F('usages') + 1)
    return HttpResponse("Recipe cooked successfully")


def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')
    recipe_id = Weight.objects.filter(~Q(product__id__contains=product_id) | Q(weight__lt=10.0)).values_list('recipe')
    recipes = Recipe.objects.filter(id__in=recipe_id)
    return render(request, 'recipes.html', {'recipes': recipes})
