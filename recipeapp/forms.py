from .models import Recipe
from django import forms


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ('slug', 'date_created', 'approval', )


