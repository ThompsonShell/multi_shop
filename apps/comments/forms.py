from django import forms
from apps.comments.models import ProductComment


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = '__all__'


