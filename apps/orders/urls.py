from django.urls import path

from apps.orders.views import checkout


urlpatterns = [
    path('', checkout, name='checkout-page'),
]