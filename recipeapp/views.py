from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.mail import send_mail, mail_admins
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from taggit.models import Tag


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class RecipeList(TagMixin, generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, approved=True).order_by('title')
    template_name = 'recipes.html'
    paginate_by = 8


class TagList(TagMixin, generic.ListView):
    model = Recipe
    template_name = 'recipes.html'

    def get_queryset(self):
        return Recipe.objects.filter(tags__slug=self.kwargs.get('tag_slug'))


class FullRecipe(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('date_posted')

        return render(
            request,
            'view_recipe.html',
            {
                'recipe': recipe,
                'comments': comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('date_posted')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.success(request, "Your comment was sent successfully. Check status below.")
        else:
            comment_form = CommentForm()
        
        return render(
            request,
            'view_recipe.html',
            {
                'recipe': recipe,
                'comments': comments,
                "commented": True,
                "comment_form": CommentForm()
            },
        )


# CRUD FOR RECIPES (R is the full recipe view above)
class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'about', 'nutrition', 'servings', 'prep_time', 'cook_time', 'ingredients', 'method', 'tags', 'status', 'featured_image', 'category', ]
    template_name = 'recipe_form.html'

    # send_mail(
    #     'Recipe approval',
    #     'A user has posted a recipe and is waiting approval',
    #     'hartnetl@tcd.ie',
    #     ['laura.codeinstitute@outlook.com'],
    #     fail_silently=False
    # )

    # mail_admins(
    #     'Recipe approval',
    #     'A user has posted a recipe and is waiting approval.',
    #     fail_silently=False
    # )

    def get_success_url(self):
        return reverse('full_recipe', kwargs={'slug': self.object.slug})


    def form_valid(self, form):
        form.instance.creator = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)


class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['title', 'slug', 'about', 'nutrition', 'servings', 'prep_time', 'cook_time', 'ingredients', 'method', 'tags', 'status', 'featured_image', 'category', ]
    template_name = 'update_recipe_form.html'

    def get_success_url(self):
        return reverse('full_recipe', kwargs={'slug': self.object.slug})


class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipe_confirm_delete.html'
    success_url = reverse_lazy("recipes")


# CRUD FOR COMMENTS (R is the full recipe view above)


# VIEWS FOR THE PROFILE PAGE - USERS RECIPES
class ProfileRecipes(View):

    def get(self, request, *args, **kwargs):
        published = Recipe.objects.filter(status=1, creator=request.user)
        draft = Recipe.objects.filter(status=0, creator=request.user)

        return render(
            request,
            'profile.html',
            {
                'published': published,
                'draft': draft
            }
        )
    
    


