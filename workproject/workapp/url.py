from django.urls import path
from workapp import views

urlpatterns=[
    path('',views.display),
    path('add/',views.regist),
    path('show/',views.show),

]