from django.urls import path
from .api import ProductListApi, ProductCreateApi



urlpatterns = [
    path("products/", ProductListApi.as_view(), name="product-list"),
    path("products/create/", ProductCreateApi.as_view(), name="product-create"),
]