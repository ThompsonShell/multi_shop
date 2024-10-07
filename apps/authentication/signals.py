from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


@receiver(user_login_failed)
def send_message_user_login_failed(*args, **kwargs):
    print('is it ok ?')
