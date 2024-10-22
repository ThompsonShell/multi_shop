from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns



from apps.main import views
from apps.categories.views import category
from apps.general.views import set_language, search, set_currency
from apps.main.views import checkout, home
from apps.products.views import product_list, detail
from apps.contacts.views import contact


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

    # ======= ADMIN URLS =======
    path('admin/', admin.site.urls),

    # ======= GENERAL URLS =======
    path('search/', include('apps.general.urls')),

    # ======= CONTACT URLS =======
    path('contacts/', include('apps.contacts.urls')),


    path('checkout/', checkout, name='checkout-page'),
    path('cart/', views.cart, name='cart-page'),


    # ======= PRODUCT URLS =======
    path('detail/', detail, name='detail-page'),

    path('search_product/', product_list, name='search_product'),

    path('products/', include('apps.products.urls', namespace='products')),

    # ======= CATEGORY URLS =======
    path('categories/', include('apps.categories.urls')),

    # ======= ABOUT URLS =======
    path('about/', include('apps.abouts.urls', namespace='about')),

    # ======= WISHLIST URLS =======
    path('wishlist/', include('apps.wishlist.urls', namespace="wishlists")),

    # =========== AUTH URLS  ============
    path('auth/', include('apps.authentication.urls')),

    # ============= DEBUG_TOOLBAR URLs =======
    path('__debug__/', include('debug_toolbar.urls')),


)
