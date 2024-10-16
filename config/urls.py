from apps.main import views
from django.contrib import admin
from django.urls import path, include
from apps.categories.views import category
from django.conf.urls.static import static
from apps.generals.views import set_language, search, set_currency
from django.conf.urls.i18n import i18n_patterns

from apps.main.views import checkout, home
from apps.products.views import product_list, detail
from apps.contacts.views import contact

from django.conf import settings

urlpatterns = [
    # =========== CKEDITOR URLS  ============
    path("__ckeditor5/", include('django_ckeditor_5.urls')),

    # =============MEDIA URLS===========
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

    # =======SET LANGUAGE URLS =======
    path('set-language/<str:lang>/', set_language, name='set-lang'),

    # =======SET CURRENCY URLS =======
    path('set-currency/<str:currency>/', set_currency, name='set-curr')

]
urlpatterns += i18n_patterns(
    path('', home, name='home-page'),
    path('search_product/', product_list, name='search_product'),
    path('admin/', admin.site.urls),
    path('search/', search, name='search_text'),
    path('detail/', detail, name='detail-page'),
    path('contact/', contact, name='contact-page'),
    path('checkout/', checkout, name='checkout-page'),
    path('cart/', views.cart, name='cart-page'),
    path('products/', include('apps.products.urls', namespace='products')),
    path('category/', category, name='category-page'),


    # ======= ABOUT URLS =======
    path('about/', include('apps.abouts.urls', namespace='about')),

    # ======= WISHLIST URLS =======
    path('wishlist/', include('apps.wishlist.urls')),

    # =========== AUTH URLS  ============
    path('auth/', include('apps.authentication.urls')),

    # ============= DEBUG_TOOLBAR URLs =======
    path('__debug__/', include('debug_toolbar.urls')),


)
