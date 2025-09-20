from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gastronomia/', views.gastronomia, name='gastronomia'),
    path('pontos/', views.pontos, name='pontosturisticos'),
]
