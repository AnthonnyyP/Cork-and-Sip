from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
     #Guests
     path('guests/', views.guests_index, name='index'),
     path('guests/<int:guest_id>/', views.guests_detail, name='detail'),
     path('guests/create/', views.GuestCreate.as_view(), name='guests_create'),
     path('guests/<int:pk>/update/',
          views.GuestUpdate.as_view(), name='guests_update'),
     path('guests/<int:pk>/delete/',
          views.GuestDelete.as_view(), name='guests_delete'),
     #Tastings
     path('guests/<int:guest_id>/add_tasting', views.add_tasting, name = 'add_tasting'),
     #Wines
     path('wines/', views.WineList.as_view(), name = 'wines_index'),
     path('wines/<int:pk>/', views.WineDetail.as_view(), name = 'wines_detail'),
     path('wines/create', views.WineCreate.as_view(), name = 'wines_create'),
     path('wines/<int:pk>/update/', views.WineUpdate.as_view(), name = 'wines_update'),
     path('wines/<int:pk>/delete/', views.WineDelete.as_view(), name = 'wines_delete'), 
     #Cellar
     path('guests/<int:guest_id>/add_to_cellar/<int:wine_id>/', views.add_to_cellar, name = "add_to_cellar"),
     path('guests/<int:guest_id>/remove_from_cellar/<int:wine_id>/', views.remove_from_cellar, name = "remove_from_cellar"),
     #Account Sign-Up
     path('accounts/signup/', views.signup, name='signup'),
]
