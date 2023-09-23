from django.urls import path
from . import views

urlpatterns = [
    path('', views.genre, name='genre'),
    path('movie/', views.movie, name='movie'),
]
