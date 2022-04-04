from django.contrib import admin

# Register your models here.

from planner.models import Menus, DayRecipe, Profile

# Register your models here.
admin.site.register(Menus)
admin.site.register(DayRecipe)
admin.site.register(Profile)
