
from django.urls import path
from .import views

urlpatterns = [

	path('',views.home,name='home'),
	path('accounts/login/',views.loginview,name="login"),
	path('logout',views.logout_view),
	path('accounts/sign_up/',views.sign_up,name="signup") ,
	path('reset',views.Resethome,name='reset'), 
	path('passwordreset',views.resetPassword,name="passwordreset")
]