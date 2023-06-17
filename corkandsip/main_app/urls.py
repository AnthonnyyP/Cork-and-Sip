from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('guests/', views.guests_index, name='index'),
    path('guests/<int:guest_id>/', views.guests_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
]
