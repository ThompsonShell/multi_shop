from django.urls import path
from .views import wishlist, delete_wishlist, create_wishlist
from ..abouts.urls import app_name

app_name = "wishlists"

urlpatterns = [
    path('', wishlist, name='wishlist'),
    path('create/<int:product_id>/', create_wishlist, name='create_wishlist'),
    path('delete/<int:product_id>/', delete_wishlist, name='delete_wishlist'),
]