from django.urls import path,include
from . import views



urlpatterns = [
    
    path('', views.index, name='home'),
    path('', include("django.contrib.auth.urls")),
    path("accounts/register/", views.register, name="register"),
    path('accounts/profile/', views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('taxExemption/', views.taxExemption, name='taxExemption'),
    path('applications/', views.applications, name='applications'),
   
]