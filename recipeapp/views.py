from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.db import transaction
from .models import Recipe
from .forms import RecipeForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('title')
    template_name = 'recipes.html'
    paginate_by = 8


class FullRecipe(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('date_posted')

        return render(
            request,
            'view_recipe.html',
            {
                'recipe': recipe,
                'comments': comments
            },
        )


class RecipeCreate(CreateView):
    model = Recipe
    add_recipe = RecipeForm()
    fields = ['title', 'creator', 'about', 'nutrition', 'servings', 'prep_time', 'cook_time', 'ingredients', 'method', 'tags', 'status', 'featured_image', 'category', ]
    template_name = 'recipe_form.html'

   
