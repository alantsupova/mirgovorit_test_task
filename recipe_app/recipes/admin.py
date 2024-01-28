from django.contrib import admin
from .models import Product, Recipe, Weight


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'usages')


class WeightInline(admin.TabularInline):
    model = Weight
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [WeightInline]
    list_display = ('title',)
