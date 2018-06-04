from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('trips/', views.trips, name='trips'),
	path('trips/<int:trip_id>/', views.trip, name='trip'),
	path('backpacks/', views.backpacks, name='backpacks'),
	path('signup/', views.signup, name='signup'),
	path('signout/', views.signout, name='signout')
]