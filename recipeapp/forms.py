from .models import Recipe, Ingredients
from django import forms


class CreateRecipe(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'about', 'nutrition', 'servings', 'prep_time', 'cook_time', 'method', 'tags', 'status', 'featured_image', 'category',)



