from django.db.models import IntegerChoices

class SocialLinkType(IntegerChoices):
    INSTAGRAM = 0, 'Instagram'
    TELEGRAM = 1, 'Telegram'
    TWITTER = 2, 'Twitter'
    YOUTUBE = 3, 'YouTube'