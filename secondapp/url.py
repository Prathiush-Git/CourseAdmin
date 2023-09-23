from django.urls import path
from secondapp import views

urlpatterns = [
    path('',views.second),
    path('call/',views.call),
]
