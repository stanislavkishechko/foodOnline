from django.urls import path
from . import views

urlpatterns = [
    path('', views.marketplace, name='marketplace'),
    path('<slug:vendor_slug>/', views.vendor_detail, name='vendor-detail'),
    path('add_to_cart/<int:food_id>/', views.add_to_cart, name='add-to-cart'),
    path('decrease_cart/<int:food_id>/', views.decrease_cart, name='decrease-cart'),
    path('delete_cart/<int:cart_id>/', views.delete_cart, name='delete-cart')
]