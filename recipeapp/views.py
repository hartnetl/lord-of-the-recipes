from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import transaction
from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
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


class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'slug', 'creator', 'about', 'nutrition', 'servings', 'prep_time', 'cook_time', 'ingredients', 'method', 'tags', 'status', 'featured_image', 'category', ]
    template_name = 'recipe_form.html'

    def get_success_url(self):
        return reverse('full_recipe', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['title', 'slug', 'creator', 'about', 'nutrition', 'servings', 'prep_time', 'cook_time', 'ingredients', 'method', 'tags', 'status', 'featured_image', 'category', ]
    template_name = 'update_recipe_form.html'

    def get_success_url(self):
        return reverse('full_recipe', kwargs={'slug': self.object.slug})


class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipe_confirm_delete.html'
    success_url = reverse_lazy("recipes")
