from django.urls import path


from apps.products.views import product_list, product_detail

app_name = 'products'



urlpatterns = [
    path('', product_list, name='product_list'),
    path('detail/<int:pk>/', product_detail, name='detail-page'),

]
