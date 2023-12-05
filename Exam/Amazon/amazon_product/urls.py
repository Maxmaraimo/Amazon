from django.urls import path

from .views import *

urlpatterns = [
    path("", ProductListView.as_view(), name="product_view"),
    path("add_product", AddProductView.as_view(), name="add_product"),
    path("update_product/<int:pk>", ProductUpdateView.as_view(), name="update_product"),
    path("product_details/<int:pk>", ProductDetailsView.as_view(), name="product_details"),
    path("delete_product/<int:book_id>", delete_book, name="delete_product")
]