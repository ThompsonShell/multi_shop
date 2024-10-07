from django.core.exceptions import PermissionDenied
from django.test import TestCase


# Create your tests here.


class UserProfile:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __delattr__(self, name):
        if hasattr(self, name) and name == 'username':

            super().__delattr__(name)


profile = UserProfile("user123", "user@example.com")
del profile.username
print(profile.username)
