from django import template

register = template.Library()


@register.simple_tag
def decimal_to_range(decimal_number):
    return range(int(decimal_number))
