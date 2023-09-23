from django.urls import path,include
from examapp import views

urlpatterns = [
    path('',views.greet),
    path('show/',views.show),
    path('display/',views.display),
]