from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_phone(phone_number: str):
    RegexValidator(
        regex=r'^\+998\d{9}$',
        message='invalid phone number'
    )














