from django.urls import path

from apps.contacts.views import contact

urlpatterns = [
    path('contact/', contact, name='contact-page'),
]
