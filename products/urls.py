from django.urls import path
from .api import ProductListApi



urlpatterns = [
    path("products/", ProductListApi.as_view(), name="product-list"),
]