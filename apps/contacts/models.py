from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True)
    title = models.CharField(max_length=150)
    message = models.TextField(max_length=10_000)

    def __str__(self):
        return self.title