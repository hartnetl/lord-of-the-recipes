from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic, View
from .models import Recipe, Ingredients
from django.views.generic import TemplateView


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('title')
    template_name = 'recipes.html'
    paginate_by = 8


class FullRecipe(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        queryset1 = recipe.ingredients.all()
        ingredients = queryset1
        comments = recipe.comments.filter(approved=True).order_by('date_posted')

        return render(
            request,
            'view_recipe.html',
            {
                'recipe': recipe,
                'ingredients': ingredients,
                'comments': comments
            },
        )

