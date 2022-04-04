from django import forms
from django.urls import reverse
from planner.models import DayRecipe, Menus, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class DayRecipeForm(forms.ModelForm):
   day = forms.DateField()
   recipe_id = forms.ModelChoiceField(queryset=DayRecipe.objects.all(),
        empty_label=None)

   class Meta:
        model = DayRecipe
        fields = "__all__"
        def __init__(self,*args,**kwargs):
             self.date = kwargs.pop('date', None)
             self.meal = kwargs.pop('meal', 0)
             user = kwargs.pop('user', None)
            
             self.fields['recipe'].queryset = Recipe.objects.filter(user__username=user)

class MenusForm(forms.ModelForm):
   model = Menus
   fields = ('meal_plann','personal_details','dietary_requirments','calories')


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']




class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']