from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns=[
    path('login/', views.Login),
    path('logout/', views.signout),
    path('signup/', views.signup),
    path('about/',views.about),
    path('base/',views.base),
    path('cart/',views.cart),
    path('checkout/',views.checkout),
    path('placeorder/',views.placeorder),
    path('contact/',views.contact),
    path('faq/',views.faq),
    path('',views.index_2),
    path('change_qty/<int:id>/', views.change_qty, name="change_qty"),
    path('order-tracking/',views.order_tracking),
    path('order/',views.order),
    path('product-details/<int:id>/',views.product_details),
    path('product-details2/',views.product_details2),
    path('product-details3/',views.product_details3),
    path('shop/',views.shop),
    path('addtocart/<int:id>/',views.addtocart),
    # path('silverring/',views.silverring),
    path('shop-list/',views.shop_list),
    path('wishlist/',views.wishlist),
    path('add_to_wishlist/<int:product_id>/',views.add_to_wishlist),
    path('search/',views.search),
    path('orderdelete/<int:id>/',views.orderdelete)

]
