from django.urls import path

from apps.comments.views import create_comment

app_name = 'comments'

urlpatterns = [
    path('create/', create_comment, name='create-comment')
]