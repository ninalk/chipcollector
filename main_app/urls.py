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
  path('chips/<int:chip_id>/assoc_store/<int:store_id>/', views.assoc_store, name='assoc_store'),
  path('chips/<int:chip_id>/unassoc_store/<int:store_id>/', views.unassoc_store, name='unassoc_store'),
  path('stores/', views.StoreList.as_view(), name='stores_index'),
  path('stores/<int:pk>/', views.StoreDetail.as_view(), name='stores_detail'),
  path('stores/create/', views.StoreCreate.as_view(), name='stores_create'),
  path('stores/<int:pk>/update/', views.StoreUpdate.as_view(), name='stores_update'),
  path('stores/<int:pk>/delete/', views.StoreDelete.as_view(), name='stores_delete'),
]