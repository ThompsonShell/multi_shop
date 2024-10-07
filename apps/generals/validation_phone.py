from django.core.exceptions import ValidationError


def validate_phone(phone_number: str):
    if not (len(phone_number) == 13
            and
            phone_number[1:].isdigit()
            and
            phone_number.startswith('+998')):
        raise ValidationError('your phone number is invalid')
