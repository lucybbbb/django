from django.contrib import admin
from .models import users, Meal_planner, Recipes, API_plugin
admin.site.register(users)
admin.site.register(Meal_planner)
admin.site.register(Recipes)
admin.site.register(API_plugin)

