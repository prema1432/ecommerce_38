from django.urls import path

from product.views import products, computer_products, product_create, cart_products, cart_product_update, delete_book

urlpatterns = [
    path("", products, name="products"),
    path("create_product/", product_create, name="create_product"),
    path("computers/", computer_products, name="computers"),
    path("cart_products/", cart_products, name="cart_products"),
    path("product_update/<int:id>/", cart_product_update, name="product_update"),
    path("book_delete/<int:id>/", delete_book, name="book_delete"),
]
