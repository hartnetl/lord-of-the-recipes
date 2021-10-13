from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('recipe/', views.RecipeList.as_view(), name='recipes'),
    path('<slug:slug>/', views.FullRecipe.as_view(), name='full_recipe'),
    path('', TemplateView.as_view(template_name="index.html")),
    path('home', TemplateView.as_view(template_name="index.html")),
    path('about', TemplateView.as_view(template_name="about.html")),
    path('contact', TemplateView.as_view(template_name="contact.html")),
    path('login', TemplateView.as_view(template_name="login.html")),
]
