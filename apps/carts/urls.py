from django.urls import path

from apps.carts.views import create_cart, delete_cart, cart, set_cart_quantity

app_name = 'carts'



urlpatterns = [
    path('', cart, name='cart'),
    path('create/<int:product_id>/', create_cart, name='create_cart'),
    path('delete/<int:product_id>/', delete_cart, name='delete_cart'),
    path('set/<int:cart_id>/', set_cart_quantity, name='set-cart-quantity')
]
