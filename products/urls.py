
from django.urls import path
from django.conf import settings
from .views import (
    home_views,
    about_view,
    ProductsView,
    product_create,
    ProductDetail,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    CheckoutView,
    remove_single_item_from_cart
)
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home_views, name="home-welcome"),
    path('about/', about_view, name="About-mcsell"),
    path('new-product/', product_create, name="new-product"),
    path('product-detail/<slug>/',
         ProductDetail.as_view(), name="product-detail"),
    path('order-summary/', OrderSummaryView.as_view(), name="order-summary"),
    path('add-to-cart/<slug>/', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>/', remove_from_cart, name="remove-from-cart"),
    path('remove-signle-item-from-cart/<slug>/',
         remove_single_item_from_cart, name="remove-signle-item-from-cart"),
    path('products/', ProductsView, name="our-products"),
    path('chechout/', CheckoutView.as_view(), name="chechout"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
