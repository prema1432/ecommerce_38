from django.urls import path
from cart.views import cart_view, wishlist

urlpatterns = [
    path("", cart_view, name="cart"),
    path("wishlist/", wishlist, name="wishlist"),

]
