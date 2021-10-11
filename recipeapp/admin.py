from django.contrib import admin
from .models import Recipe, Ingredients, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


class IngredientInline(admin.TabularInline):
    model = Ingredients


# class CategoryInline(admin.TabularInline):
#     model = Category


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'date_created', 'approval', 'category')
    search_fields = ['title', 'about', 'method', 'ingredients__item', 'category']
    list_display = ('title', 'slug', 'status', 'date_created')
    summernote_fields = ('about', 'method', 'nutrition')
    inlines = [IngredientInline, ]

    actions = ['approve_recipes']

    def approve_recipes(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Category)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('approved',)
    search_fields = ['name', 'email', 'message']
    list_display = ('name', 'message', 'recipe', 'date_posted', 'approved')
    summernote_fields = ('message')

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
