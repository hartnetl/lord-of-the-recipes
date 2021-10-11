from django.contrib import admin
from .models import Recipe, Ingredients, Category
from django_summernote.admin import SummernoteModelAdmin


class IngredientInline(admin.TabularInline):
    model = Ingredients


class CategoryInline(admin.TabularInline):
    model = Category


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'date_created', 'approval', 'categories__name')
    search_fields = ['title', 'about', 'method', 'ingredients__item', 'categories__name']
    list_display = ('title', 'slug', 'status', 'date_created')
    summernote_fields = ('about', 'method', 'nutrition')
    inlines = [IngredientInline, CategoryInline, ]
