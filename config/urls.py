from apps.main import views
from django.contrib import admin
from django.urls import path, include
from apps.categories.views import category
from django.conf.urls.static import static
from apps.generals.views import set_language, search
from django.conf.urls.i18n import i18n_patterns

from config import settings

urlpatterns = [
    # =========== CKEDITOR URLS  ============
    path("__ckeditor5/", include('django_ckeditor_5.urls')),

    # =============MEDIA URLS===========
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

    # =======SET LANGUAGE URLS =======
    path('set-language/<str:lang>/', set_language, name='set-lang'),

]
urlpatterns += i18n_patterns(
    path('', views.home, name='home-page'),
    path('admin/', admin.site.urls),
    path('search/', search, name='search_text'),
    path('detail/', views.detail, name='detail-page'),
    path('contact/', views.contact, name='contact-page'),
    path('checkout/', views.checkout, name='checkout-page'),
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
