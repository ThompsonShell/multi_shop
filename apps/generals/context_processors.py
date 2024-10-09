from apps.generals.models import General, GeneralSocialMedia
from apps.wishlist.models import Wishlist


def general_context(request):
    context = {
        'generals': General.objects.all(),
        'wishlist_count': Wishlist.objects.filter(user=request.user).count() if request.user.is_authenticated else 0,
        'general_social_media': GeneralSocialMedia.objects.all()
    }
    return context