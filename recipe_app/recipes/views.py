from django.shortcuts import render
from django.http import HttpResponse



def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    # Ваша логика добавления продукта к рецепту

    return HttpResponse("Product added to recipe successfully")


def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')

    # Ваша логика увеличения количества приготовленных блюд для каждого продукта

    return HttpResponse("Recipe cooked successfully")


def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')

    # Ваша логика получения списка рецептов без указанного продукта
