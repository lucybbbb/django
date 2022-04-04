from django.urls import path
from .views import HomePageView, select_food,add_food,ProfilePage,update_food,delete_food

from . import views
app_name ='calories'

urlpatterns = [
  path('calories/home1/', views.HomePageView,name='home1'),
  #path('login/',LoginPage,name='login'),
  #path('logout/',LogOutPage,name='logout'),
  path('select_food/',select_food,name='select_food'),
  path('add_food/',add_food,name='add_food'),
  path('update_food/<str:pk>/',update_food,name='update_food'),
  path('delete_food/<str:pk>/',delete_food,name='delete_food'),
  #path('register/',RegisterPage,name='register'),
  path('profile/',ProfilePage,name='profile'),
]

