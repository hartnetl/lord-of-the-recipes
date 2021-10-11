from django.contrib import admin
from .models import Recipe, Ingredients, Category


class IngredientInline(admin.TabularInline):
    model = Ingredients


class CategoryInline(admin.TabularInline):
    model = Category


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, CategoryInline, ]
