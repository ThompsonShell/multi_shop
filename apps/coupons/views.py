from django.contrib import messages

from django.shortcuts import render, redirect

from apps.coupons.models import Coupon, UsedCoupon


def check_coupon(request):
    code = request.POST.get('coupon_code')

    if code is None:
        return redirect('home-page')

    try:
        coupon = Coupon.objects.get(code=code)
    except Coupon.DoesNotExist:
        if request.session.get('coupon_code'):
            del request.session['coupon_code']
        messages.error(request, 'Coupon code does not exist')
    else:
        if UsedCoupon.objects.filter(
                coupon_id=coupon.pk,
                user_id=request.user.pk
        ).exists():
            if request.session.get('coupon_code'):
                del request.session['coupon_code']
                messages.warning(request, 'this coupon has already been used')
        else:
            request.session['coupon_code'] = {
                'code': coupon.code,
                'discount_percent': coupon.discount_percent,
            }
        print(request.session['coupon_code'])
        messages.success(request, 'success')


    return redirect(request.META['HTTP_REFERER'])