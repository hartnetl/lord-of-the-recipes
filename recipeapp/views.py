from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.db import transaction
from .models import Recipe
from .forms import RecipeForm, IngredientsFormSet


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


class RecipeCreate(CreateView):
    model = Recipe
    exclude = ('slug', 'approval',)


class RecipeWithIngredients(CreateView):
    model = Recipe
    fields = ['title', 'about', 'nutrition', 'servings' , 'prep_time', 'cook_time' , 'method', 'tags' , 'status' , 'featured_image' , 'category', ]
    template_name = 'recipe_form.html'

    def get_context_data(self, **kwargs):
        data = super(RecipeWithIngredients, self).get_context_data(**kwargs)
        if self.request.POST:
            data['fullrecipe'] = IngredientsFormSet(self.request.POST)
        else:
            data['fullrecipe'] = IngredientsFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        fullrecipe = context['fullrecipe']
        with transaction.atomic():
            self.object = form.save()

            if fullrecipe.is_valid():
                fullrecipe.instance = self.object
                fullrecipe.save()
        return super(RecipeWithIngredients, self).form_valid(form)
