from apps.generals.models import General, GeneralSocialMedia
from apps.products.models import Product
from apps.wishlist.models import Wishlist


def general_context(request):
    context = {
        'generals': General.objects.all(),
        'general_social_media': GeneralSocialMedia.objects.all(),
        'currency': request.session.get('currency', Product.DEFAULT_CURRENCY),
        'currency_list': Product.Currency.labels,
    }
    return context