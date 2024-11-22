from apps.carts.models import Cart


def carts_context(request):
    context = {
        'carts_count': Cart.objects.filter(user=request.user).count() if request.user.is_authenticated else 0,
    }
    return context