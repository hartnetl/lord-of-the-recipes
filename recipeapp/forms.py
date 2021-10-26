from .models import Recipe, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextField


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ('slug', 'date_created', 'approval', )
        widgets = {
            'about': SummernoteWidget(),
            'method': SummernoteWidget(),
            'nutrition': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)


class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


# class EditForm(forms.Form):
#     edit = forms.CharField(widget=SummernoteInplaceWidget())