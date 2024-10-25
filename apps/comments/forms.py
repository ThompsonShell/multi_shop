from django import forms

from apps.comments.models import ProductComment


class CommentCreateForm(forms.ModelForm):
    models = ProductComment
    fields = '__all__'