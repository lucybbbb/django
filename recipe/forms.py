
from django import forms
from django.urls import reverse
from planner.models import Recipe, Topic



class TopicForm(forms.ModelForm):
    title=forms.CharField()


class RecipeForm(forms.ModelForm):
    title=forms.CharField()
    description =forms.CharField()
    ingredients = forms.CharField()
    topic = forms.CharField()

    class Meta()
      model=recipe
      fields =['title', 'ingredients','description','topic']















