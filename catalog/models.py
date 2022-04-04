from django.db import models
from django.urls import reverse


class users(models.Model):
    id = models.CharField( max_length=200, primary_key=True, default = None)
    first_name = models.TextField(max_length=100,default =None)
    last_name = models.TextField(max_length=100)
    created_at =models.DateTimeField(default =None)
    email_address = models.EmailField(max_length=200,default =None)
    password = models.CharField(max_length=100,default =None)
    DOB = models.DateField(max_length = 50,default =None)
    chosen_diets = models.CharField(max_length=200,default =None)
    intolerances = models.CharField(max_length = 200,default =None)
    Desired_meal_plan_lenght = models.DateField()
    Desired_meal_type = models.TextField(max_length = 200,default =None)

    def __str__(self):
        return self.id
   


class Meal_planner(models.Model):
    meal_plan = models.CharField(max_length = 200,default =None)
    id = models.ForeignKey('users', on_delete=models.CASCADE, primary_key=True)
    
    recipe_id = models.CharField(max_length =200,default =None)
    meals_within_diet = models.TextField(max_length =300,default =None)
    shopping_basket = models.TextField(max_length = 300,default =None)
    total_recipe_portions = models.IntegerField(default =None)
    consumed_portions_size = models.IntegerField(default =None)
    calories_per_serving = models.IntegerField(default =None)
    total_daily_calories = models.IntegerField(default =None)
    total_weekly_calories = models.IntegerField(default =None)
    total_montly_calories = models.IntegerField(default =None)
    cooking_time_per_meal = models.TimeField(default =None)
    total_cooking_time_per_day = models.TimeField(default =None)
    day_meals_were_consumed = models.DateTimeField()


    def __str__(self):
      return self.meals_within_diet
    
class Recipes(models.Model):
    recipe_id = models.ForeignKey('Meal_planner', on_delete = models.CASCADE, default=None)
    API_plugin_id = models.IntegerField(default =None)
    all_meals_imported = models.TextField(default =None)
    recipe_name = models.TextField(default =None)
    meal_description = models.TextField(default =None)
    ingredients_and_quantity = models.TextField(default =None)
    cooking_time = models.TimeField(default =None)
    meal_recipe_full_calories = models.IntegerField(default =None)


  
    def get_url(self):
        return reverse("RECIPE", self.recipe_name )

class  API_plugin(models.Model):
    API_plugin_id = models.ForeignKey('Recipes', on_delete = models.CASCADE,default =None)
    recipe_websites = models.TextField(default =None)
    recipe_hyperlinks = models.TextField(default =None)
    supermarket_websites = models.TextField(default =None)
  
  

    def get_url(self):
        return reverse("website", self.recipe_website )


