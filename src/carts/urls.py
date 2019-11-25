from django.urls import path

from . import views


urlpatterns = [
    path('add_to_cart/<int:id>', views.AddToCart, name='add'),
    path('cart_count', views.cart_count, name='cart_count'),
    path('AddCartMultiple', views.AddCartMultiple, name='cart_multiple'),

]
