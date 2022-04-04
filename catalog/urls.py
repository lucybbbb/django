from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  
    path('login', views.login_user, name='login'),
    path('register/' ,views.register_request,  name="signup"),
    path('index/', views.index, name='home'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('password_change_done/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('dietreq', views.dietreq, name='dietreq'),
    
]
   
urlpatterns += staticfiles_urlpatterns()