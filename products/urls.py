from django.urls import path
from .api import ProductListApi, ProductCreateApi, ProductDetailApi, ProductDeleteApi, ProductUpdateApi



urlpatterns = [
    path("products/", ProductListApi.as_view(), name="product-list"),
    path("products/create/", ProductCreateApi.as_view(), name="product-create"),
    path("products/<int:pk>/", ProductDetailApi.as_view(), name="product-detail"),
    path("products/<int:pk>/update/", ProductUpdateApi.as_view(), name="product-update"),
    path("products/<int:pk>/delete/", ProductDeleteApi.as_view(), name="product-delete"),
]