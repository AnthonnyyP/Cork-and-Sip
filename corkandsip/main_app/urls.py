from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('guests/', views.guests_index, name='index'),
    path('guests/<int:guest_id>/', views.guests_detail, name='detail'),
    path('guests/create/', views.GuestCreate.as_view(), name='guests_create'),
    path('guests/<int:pk>/update/',
         views.GuestUpdate.as_view(), name='guests_update'),
    path('guests/<int:pk>/delete/',
         views.GuestDelete.as_view(), name='guests_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
