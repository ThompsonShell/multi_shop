from apps.general.models import General, GeneralSocialMedia
from apps.products.models import Product
from apps.wishlist.models import Wishlist


def general_context(request):
    context = {
        'generals': General.objects.all(),
        'general_social_media': GeneralSocialMedia.objects.all(),
        'currency': request.session.get('currency', General.DEFAULT_CURRENCY),
        'currency_list': General.Currency.labels,
    }
    return context