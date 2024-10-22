from django.urls import path

from apps.general.views import search

urlpatterns = [
    path('search/', search, name='search_text'),
]
