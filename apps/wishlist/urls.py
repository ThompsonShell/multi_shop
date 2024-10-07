from django.urls import path
from .views import wishlist, delete_wishlist, create_wishlist

urlpatterns = [
    path('', wishlist, name='wishlist'),
    path('create/<int:product_id>/', create_wishlist, name='create_wishlist'),
    path('delete/<int:_id>/', delete_wishlist, name='delete_wishlist'),
]