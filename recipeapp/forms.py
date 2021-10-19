from .models import Recipe, Comment
from django import forms


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ('slug', 'date_created', 'approval', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)