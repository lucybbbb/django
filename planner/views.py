from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import CreateView
import datetime

from django.contrib.auth.models import User
from planner.models import DayRecipe,Menus, Profile

from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views import View
from .models import Recipes
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .forms import UpdateUserForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages
#class PlannerHomeView(LoginRequiredMixin, RedirectView):
 #   context = {}
  #  template_name='meal_editor.css'
   #   
    #def get(self,request):
     #   return render(request,'meal_editor.css')
      
      
      

#class RecipeView(LoginRequiredMixin,View):
 #   def get(self, request):
  #      recipes = Recipes.objects.all()
   #     context = {'recipes': recipes}
    #    return render(request, 'planner_day.css')
       
class MenusListView(ListView):
    model = Menus
    context_object_name = 'menus'
    template_name = "account.css"
   
   
def MealView(request):
   return render(request,'recipe.css')

def DietaryView(request):
    return render(request, 'dietary.css')

def PlannerHomeView(request):
    return render(request,'meal_editor.css')
def RecipeView(request):
    return render(request, 'planner_day.css')

@login_required
def profile(request):
        #return render(request, 'profile.css')
 Profile.objects.get_or_create(user=request.user)
 if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to ='users-profile')
 else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

 return render(request, 'profile.css', {'user_form': user_form, 'profile_form': profile_form})

 