from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        min_length=4,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'autofocus': 'autofocus', })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
        })
    )
    password = forms.CharField(
        min_length=8,
        required=True,
        validators=[validate_password],
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',

        })
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        # kwargs = {
        #         CustomUser.USERNAME_FIELD: username,
        # }
        if get_user_model().objects.filter(username=username).exists(): #filter(**kwargs)f
            raise forms.ValidationError('Username already exists')
        return username


