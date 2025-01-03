from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from apps.carts.models import Cart
from apps.wishlist.models import Wishlist
from apps.comments.models import ProductComment
from apps.products.models import Product
from apps.products.models import ProductFeatures
from apps.features.models import Feature


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = ProductComment.objects.filter(product_id=product.pk).order_by('-pk')
    image = Product.objects.get(pk=product.pk).main_image
    comment_page = request.GET.get('comment_page', 1)
    comment_page_obj = Paginator(comments, 3).get_page(comment_page)
    try:
        user_cart_quantity = Cart.objects.get(product_id=pk, user=request.user).quantity
    except Cart.DoesNotExist:
        user_cart_quantity = 0

    context = {
        'image': image,
        'product': product,
        'user_cart_quantity': user_cart_quantity,
        'page': 'detail',
        'comments': comments,
        'comment_page_obj': comment_page_obj

    }
    return render(request=request, template_name='detail.html', context=context)


def product_by_feature(request, pk):
    print(request.POST)
    return redirect('products:detail-page', pk=pk)


def product_list(request: WSGIRequest) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        user_wishlist = Wishlist.objects.filter(user_id=user.pk).values_list('product_id', flat=True)
    else:
        user_wishlist = []

    search_text = request.session.get('search_text', None)
    queryset = Product.objects.order_by('-pk')

    if search_text:
        queryset = queryset.filter(title__icontains=search_text).values()

    page_number = request.GET.get('page', 1)
    page_number = int(page_number)
    paginate_obj = Paginator(queryset, 9)
    page_obj = paginate_obj.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'page': 'shop',
        'user_wishlist': user_wishlist,

    }
    return render(request=request, template_name='shop.html', context=context)

