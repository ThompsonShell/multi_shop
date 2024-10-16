from apps.generals.models import General, GeneralSocialMedia
from apps.wishlist.models import Wishlist


def wishlists_context(request):
    context = {
        'wishlist_count': Wishlist.objects.filter(user=request.user).count() if request.user.is_authenticated else 0,
    }
    return context