from django.db import models
from  autoslug import AutoSlugField
from django.shortcuts import reverse

class Topic(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title")
    
    #def __str__(self):
     #   return self.title
    
    class Meta:
        ordering=('title',)

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title")
    image = models.ImageField(max_length=400, upload_to='media/images')
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    servings = models.CharField(max_length=5)
    time = models.CharField(max_length=5)
    calories = models.CharField(max_length=5)
    fat = models.CharField(max_length=5)
    carbs = models.CharField(max_length=5)
    protein = models.CharField(max_length=5)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

   
    class Meta:
        ordering=('topic',)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
      return reverse("recipe_detail", args=[str(self.id)])

  



