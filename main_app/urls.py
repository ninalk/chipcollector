from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chips/', views.chips_index, name='index'),
  path('chips/<int:chip_id>/', views.chips_detail, name='detail'),
  path('chips/create/', views.ChipCreate.as_view(), name='chips_create'),
  path('chips/<int:pk>/update/', views.ChipUpdate.as_view(), name='chips_update'),
  path('chips/<int:pk>/delete/', views.ChipDelete.as_view(), name='chips_delete'),
  path('chips/<int:chip_id>/add_review/', views.add_review, name='add_review'),
]