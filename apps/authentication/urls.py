from django.urls import path
from apps.authentication.views import *

urlpatterns = [

    path('login_page/', login_page, name='login-page'),
    path('login/', user_login, name='user_login'),
    path('logout/', logout_page, name='logout-page'),
    path('register_page/', register_page, name='register-page'),
    path('register/', user_register, name='user-register'),

]

# if settings.DEBUG:
