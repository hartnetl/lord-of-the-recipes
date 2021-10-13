from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('recipe/', views.RecipeList.as_view(), name='recipes'),
    path('<slug:slug>/', views.FullRecipe.as_view(), name='full_recipe'),
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('about', TemplateView.as_view(template_name="about.html"), name="about"),
    path('contact', TemplateView.as_view(template_name="contact.html"), name="contact"),
    path('login', TemplateView.as_view(template_name="login.html"), name="login"),
]
