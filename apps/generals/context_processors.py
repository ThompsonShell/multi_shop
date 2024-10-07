from apps.generals.models import General, GeneralSocialMedia


def general_context(request):
    context = {
        'generals': General.objects.all(),
        'general_social_media': GeneralSocialMedia.objects.all()
    }
    return context