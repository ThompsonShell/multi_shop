from django import template

from decimal import Decimal

from apps.general.models import CurrencyAmount, General
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
def get_price_by_currency(to_currency: str = General.Currency.UZS, price: Decimal = 0) -> Decimal:
    if to_currency == General.Currency.UZS:
        return price
    return round(price / Decimal(CurrencyAmount.get_amount(currency=to_currency)), 2)


@register.simple_tag
def stars_by_amount(rating: int) -> str:
    return '0' * rating
