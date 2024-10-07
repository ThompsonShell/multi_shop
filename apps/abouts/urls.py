
from django.urls import path

from apps.abouts import views

app_name='about'

urlpatterns = [
    path('', views.about, name='about-page'),
]