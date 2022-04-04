from django.urls import path
from recipe.views import search,  recipe_list 
from .import views

from django.conf import settings
from django.conf.urls.static import static


app_name ='recipe'
urlpatterns = [
   
    
    path('recipe_list', views.recipe_list, name="recipe_list"),
    path('recipe/<int:pk>',views.RecipeDetailView.as_view(), name='recipe_detail'),
    #path('search/recipe_detail/', views.recipe_detail, name="recipe_detail"),
    path('search/', views.search, name="search"),
   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)