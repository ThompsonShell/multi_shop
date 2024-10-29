from django import template

from decimal import Decimal
from apps.wishlist.models import Wishlist

register = template.Library()


@register.simple_tag
def decimal_to_range(decimal_number):
    if isinstance(decimal_number, int):
        return range(decimal_number)


@register.simple_tag
def product_in_wishlist(user_id: int, product_id: int) -> bool:
    return Wishlist.objects.filter(user_id=user_id, product_id=product_id).exists()


@register.simple_tag
def get_price_by_currency(to_currency: str, price: Decimal = 0) -> bool:
    return price * 10