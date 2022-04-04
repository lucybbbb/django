from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings
from .views import profile


app_name ='planner'
urlpatterns = [

    path('RecipeView', views.RecipeView, name='planner_day'),
    path('PlannerHomeView', views.PlannerHomeView, name='meal_editor'),
    path('MenusListView', views.MenusListView.as_view(), name='account'),
    path('Mealview', views.MealView, name='recipe'),
    path('DietaryView', views.DietaryView, name='dietary'),
    path('profile/', profile, name='users-profile'),
 

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)