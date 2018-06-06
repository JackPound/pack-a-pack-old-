from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('trips/', views.trips, name='trips'),
	path('trips/<int:trip_id>/', views.trip, name='trip'),
	path('backpacks/', views.backpacks, name='backpacks'),
	path('backpacks/<int:pack_id>', views.backpack, name='backpack'),
	path('signup/', views.signup, name='signup'),
	path('signout/', views.signout, name='signout'),
	path('remove/<int:pack_id>/<int:trip_id>', views.remove_pack, name='remove_pack'),
	path('add_pack/', views.add_pack, name='add_pack'),
	path('create_pack/', views.create_pack, name='create_pack'),
	path('delete_pack/<int:pack_id>', views.delete_pack, name='delete_pack'),
	path('pack_item/<int:pack_id>/<int:item_id>/', views.pack_item, name='pack_item'),
	path('unpack_item/', views.unpack_item, name='unpack_item')
]