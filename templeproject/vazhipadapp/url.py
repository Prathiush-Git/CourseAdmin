from django.urls import path
from vazhipadapp import views   

urlpatterns = [
    path('',views.add),
    path('aa/',views.aa),
    path('vieww/',views.vieww),
    path('update/(?P<pk>\w+)',views.update,name="update"),
    path('delete/(?P<pk>\w+)',views.delete,name="delete"),
]