from django.urls import path

from product.views import products, computer_products

urlpatterns = [
    path("", products, name="products"),
    path("computers/", computer_products, name="computers"),

]
