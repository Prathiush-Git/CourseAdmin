from django.urls import path
from newapp import views

urlpatterns = [
    path('',views.display),
    path('show/',views.show)
]
