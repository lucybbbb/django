from django.urls import path,include
from . import views

app_name ='calculator'
urlpatterns = [
    path('',views.home, name='home'),
    path('user/',views.userPage, name='userPage'),
    path('product/', views.fooditem, name='fooditem'),
    path('createfooditem/',views.createfooditem, name='createfooditem'),
    path('addFooditem/', views.addFooditem, name='addFooditem'),

]