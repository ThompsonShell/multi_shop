from django.urls import path

from apps.categories.views import category


urlpatterns = [
    path('category/', category, name='category-page'),
]
