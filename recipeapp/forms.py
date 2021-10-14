from .models import Recipe, Ingredients
from django import forms
from django.forms.models import inlineformset_factory


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ()

class IngredientsForm(forms.ModelForm):

    class Meta:
        model = Ingredients()
        exclude = ()

IngredientsFormSet = inlineformset_factory(Recipe, Ingredients,
                                          form=IngredientsForm, extra=1 )


