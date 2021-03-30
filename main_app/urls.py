from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chips/', views.chips_index, name='index'),
  path('chips/<int:chip_id>/', views.chips_detail, name='detail'),
]