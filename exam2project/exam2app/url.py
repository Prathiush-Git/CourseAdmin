from django.urls import path
from exam2app import views

urlpatterns = [
    path('',views.greet),
]