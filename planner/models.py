from django.db import models
from catalog.models import Recipes
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save
from PIL import Image

class DayRecipe(models.Model):

    BREAKFAST = 0
    LUNCH = 1
    DINNER = 2
    MEAL_CHOICES = (
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
    )

    day = models.DateField()
    recipe_id = models.ForeignKey('catalog.Recipes', on_delete=models.CASCADE)
    meal_plan = models.CharField(max_length = 150, default=DINNER)

    def __unicode__(self):
        return self.day.date.isoformat() + ' - ' + self.recipe.__unicode__()


class Menus(models.Model):
    meal_plan=models.OneToOneField('Dayrecipe',on_delete=models.CASCADE)
    personal_details=models.CharField(max_length=100)
    dietary_requiremennts=models.CharField(max_length=100)
    calorie_statistics=models.IntegerField()

    def __self__():
        return self.meal_plan

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField( default = "Default.jpg", upload_to='media/images')
    def __str__(self):
         return self.user.username
    
    def save(self, *args, **kwargs):
      super().save()

      img = Image.open(self.avatar.path)

      if img.height > 100 or img.width > 100:
        new_img = (100, 100)
        img.thumbnail(new_img)
        img.save(self.avatar.path) 