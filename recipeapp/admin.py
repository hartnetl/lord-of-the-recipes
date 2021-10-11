from django.contrib import admin
from .models import Recipe, Ingredients, Category
from django_summernote.admin import SummernoteModelAdmin


class IngredientInline(admin.TabularInline):
    model = Ingredients


class CategoryInline(admin.TabularInline):
    model = Category


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('about', 'method', 'nutrition')
    inlines = [IngredientInline, CategoryInline, ]
