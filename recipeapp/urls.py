from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('create/', views.RecipeCreate.as_view(), name='create'),
    path('recipe/', views.RecipeList.as_view(), name='recipes'),
    path('profile/', views.ProfileRecipes.as_view(), name='profile'),
    path('<slug:slug>/', views.FullRecipe.as_view(), name='full_recipe'),
    path('<slug:slug>/update/', views.RecipeUpdate.as_view(), name='update'),
    path('<slug:slug>/delete/', views.RecipeDelete.as_view(), name='delete'),
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('about', TemplateView.as_view(template_name="about.html"), name="about"),
    path('contact', TemplateView.as_view(template_name="contact.html"), name="contact"),
    path('login', TemplateView.as_view(template_name="login.html"), name="login"),
    path('tags/<slug:tag_slug>/', views.TagList.as_view(), name="recipes_by_tag"),
    # path('categories/<slug:category_slug>/', views.CategoryView.as_view(), name="recipes_by_category"),
    path('recipe/breakfast/', views.BreakfastView.as_view(), name="breakfast"),
]
