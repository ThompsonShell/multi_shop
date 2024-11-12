from django.urls import path

from apps.contacts.views import contact, create_comment
from apps.products.urls import app_name

app_name = 'contacts'

urlpatterns = [
    path('contact/', contact, name='contact-page'),
    path('create-contact/', create_comment, name='create_comment')
]
