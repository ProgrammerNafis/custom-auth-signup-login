from django.urls import path
from .views import *
urlpatterns = [
    path('add/<pk>', addToCart,name='add'),
    path('cart',cart_view,name='cart'),
    path('remove/<pk>',remove,name='remove'),
    path('increase/<pk>',increase_cart,name='increase'),
    path('decrease/<pk>',decrease_cart,name='decrease')
]