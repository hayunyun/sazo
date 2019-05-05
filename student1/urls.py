from django.urls import path
from . import views


urlpatterns = [
    path('recommended/', views.first, name="first"),
    path('random_results/', views.random_results, name="random_results"),
    
    
    
]