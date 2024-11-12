from django import forms
from apps.contacts.models import Contact


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'message']


